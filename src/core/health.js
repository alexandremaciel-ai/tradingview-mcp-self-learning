/**
 * Core health/discovery/launch logic.
 */
import { getClient, getTargetInfo, evaluate } from '../connection.js';
import { existsSync } from 'fs';
import { execSync, spawn } from 'child_process';

export async function healthCheck() {
  await getClient();
  const target = await getTargetInfo();

  const state = await evaluate(`
    (function() {
      var result = { url: window.location.href, title: document.title };
      try {
        var chart = window.TradingViewApi._activeChartWidgetWV.value();
        result.symbol = chart.symbol();
        result.resolution = chart.resolution();
        result.chartType = chart.chartType();
        result.apiAvailable = true;
      } catch(e) {
        result.symbol = 'unknown';
        result.resolution = 'unknown';
        result.chartType = null;
        result.apiAvailable = false;
        result.apiError = e.message;
      }
      return result;
    })()
  `);

  return {
    success: true,
    cdp_connected: true,
    target_id: target.id,
    target_url: target.url,
    target_title: target.title,
    chart_symbol: state?.symbol || 'unknown',
    chart_resolution: state?.resolution || 'unknown',
    chart_type: state?.chartType ?? null,
    api_available: state?.apiAvailable ?? false,
  };
}

export async function discover() {
  const paths = await evaluate(`
    (function() {
      var results = {};
      try {
        var chart = window.TradingViewApi._activeChartWidgetWV.value();
        var methods = [];
        for (var k in chart) { if (typeof chart[k] === 'function') methods.push(k); }
        results.chartApi = { available: true, path: 'window.TradingViewApi._activeChartWidgetWV.value()', methodCount: methods.length, methods: methods.slice(0, 50) };
      } catch(e) { results.chartApi = { available: false, error: e.message }; }
      try {
        var col = window.TradingViewApi._chartWidgetCollection;
        var colMethods = [];
        for (var k in col) { if (typeof col[k] === 'function') colMethods.push(k); }
        results.chartWidgetCollection = { available: !!col, path: 'window.TradingViewApi._chartWidgetCollection', methodCount: colMethods.length, methods: colMethods.slice(0, 30) };
      } catch(e) { results.chartWidgetCollection = { available: false, error: e.message }; }
      try {
        var ws = window.ChartApiInstance;
        var wsMethods = [];
        for (var k in ws) { if (typeof ws[k] === 'function') wsMethods.push(k); }
        results.chartApiInstance = { available: !!ws, path: 'window.ChartApiInstance', methodCount: wsMethods.length, methods: wsMethods.slice(0, 30) };
      } catch(e) { results.chartApiInstance = { available: false, error: e.message }; }
      try {
        var bwb = window.TradingView && window.TradingView.bottomWidgetBar;
        var bwbMethods = [];
        if (bwb) { for (var k in bwb) { if (typeof bwb[k] === 'function') bwbMethods.push(k); } }
        results.bottomWidgetBar = { available: !!bwb, path: 'window.TradingView.bottomWidgetBar', methodCount: bwbMethods.length, methods: bwbMethods.slice(0, 20) };
      } catch(e) { results.bottomWidgetBar = { available: false, error: e.message }; }
      try {
        var replay = window.TradingViewApi._replayApi;
        results.replayApi = { available: !!replay, path: 'window.TradingViewApi._replayApi' };
      } catch(e) { results.replayApi = { available: false, error: e.message }; }
      try {
        var alerts = window.TradingViewApi._alertService;
        results.alertService = { available: !!alerts, path: 'window.TradingViewApi._alertService' };
      } catch(e) { results.alertService = { available: false, error: e.message }; }
      return results;
    })()
  `);

  const available = Object.values(paths).filter(v => v.available).length;
  const total = Object.keys(paths).length;

  return { success: true, apis_available: available, apis_total: total, apis: paths };
}

export async function uiState() {
  const state = await evaluate(`
    (function() {
      var ui = {};
      var bottom = document.querySelector('[class*="layout__area--bottom"]');
      ui.bottom_panel = { open: !!(bottom && bottom.offsetHeight > 50), height: bottom ? bottom.offsetHeight : 0 };
      var right = document.querySelector('[class*="layout__area--right"]');
      ui.right_panel = { open: !!(right && right.offsetWidth > 50), width: right ? right.offsetWidth : 0 };
      var monacoEl = document.querySelector('.monaco-editor.pine-editor-monaco');
      ui.pine_editor = { open: !!monacoEl, width: monacoEl ? monacoEl.offsetWidth : 0, height: monacoEl ? monacoEl.offsetHeight : 0 };
      var stratPanel = document.querySelector('[data-name="backtesting"]') || document.querySelector('[class*="strategyReport"]');
      ui.strategy_tester = { open: !!(stratPanel && stratPanel.offsetParent) };
      var widgetbar = document.querySelector('[data-name="widgetbar-wrap"]');
      ui.widgetbar = { open: !!(widgetbar && widgetbar.offsetWidth > 50) };
      ui.buttons = {};
      var btns = document.querySelectorAll('button');
      var seen = {};
      for (var i = 0; i < btns.length; i++) {
        var b = btns[i];
        if (b.offsetParent === null || b.offsetWidth < 15) continue;
        var text = b.textContent.trim();
        var aria = b.getAttribute('aria-label') || '';
        var dn = b.getAttribute('data-name') || '';
        var label = text || aria || dn;
        if (!label || label.length > 60) continue;
        var key = label.replace(/[^a-zA-Z0-9 ]/g, '').substring(0, 40);
        if (seen[key]) continue;
        seen[key] = true;
        var rect = b.getBoundingClientRect();
        var region = 'other';
        if (rect.y < 50) region = 'top_bar';
        else if (rect.y < 90 && rect.x < 650) region = 'toolbar';
        else if (rect.x < 45) region = 'left_sidebar';
        else if (rect.x > 650 && rect.y < 100) region = 'pine_header';
        else if (rect.y > 750) region = 'bottom_bar';
        if (!ui.buttons[region]) ui.buttons[region] = [];
        ui.buttons[region].push({ label: label.substring(0, 40), disabled: b.disabled, x: Math.round(rect.x), y: Math.round(rect.y) });
      }
      ui.key_buttons = {};
      var keyLabels = {
        'add_to_chart': /add to chart/i, 'save_and_add': /save and add/i,
        'update_on_chart': /update on chart/i, 'save': /^Save(Save)?$/,
        'saved': /^Saved/, 'publish_script': /publish script/i,
        'compile_errors': /error/i, 'unsaved_version': /unsaved version/i,
      };
      for (var i = 0; i < btns.length; i++) {
        var b = btns[i];
        if (b.offsetParent === null) continue;
        var text = b.textContent.trim();
        for (var k in keyLabels) {
          if (keyLabels[k].test(text)) {
            ui.key_buttons[k] = { text: text.substring(0, 40), disabled: b.disabled, visible: b.offsetWidth > 0 };
          }
        }
      }
      try {
        var chart = window.TradingViewApi._activeChartWidgetWV.value();
        ui.chart = { symbol: chart.symbol(), resolution: chart.resolution(), chartType: chart.chartType(), study_count: chart.getAllStudies().length };
      } catch(e) { ui.chart = { error: e.message }; }
      try {
        var replay = window.TradingViewApi._replayApi;
        function unwrap(v) { return (v && typeof v === 'object' && typeof v.value === 'function') ? v.value() : v; }
        ui.replay = { available: unwrap(replay.isReplayAvailable()), started: unwrap(replay.isReplayStarted()) };
      } catch(e) { ui.replay = { error: e.message }; }
      return ui;
    })()
  `);

  return { success: true, ...state };
}

/**
 * Check if TradingView is currently running (platform-aware).
 * Returns { running: boolean, pids: number[], hasCdp: boolean }
 */
async function detectRunningTV(cdpPort) {
  const platform = process.platform;
  let running = false;
  let pids = [];

  try {
    if (platform === 'win32') {
      const out = execSync('tasklist /FI "IMAGENAME eq TradingView.exe" /NH', { timeout: 3000 }).toString();
      const matches = out.match(/TradingView\.exe\s+(\d+)/g);
      if (matches) {
        pids = matches.map(m => parseInt(m.match(/(\d+)/)[1]));
        running = pids.length > 0;
      }
    } else {
      // Use pgrep to find TradingView binary processes only (not Node.js MCP server)
      const out = execSync("pgrep -f 'TradingView.app/Contents/MacOS/TradingView|/opt/TradingView/|/.local/share/TradingView/' 2>/dev/null || true", { timeout: 3000 }).toString().trim();
      if (out) {
        pids = out.split('\n').map(Number).filter(Boolean);
        running = pids.length > 0;
      }
    }
  } catch { /* ignore */ }

  // Check if CDP is actually responding on the port
  let hasCdp = false;
  try {
    const http = await import('http');
    hasCdp = await new Promise((resolve) => {
      const req = http.get(`http://localhost:${cdpPort}/json/version`, (res) => {
        let data = '';
        res.on('data', (chunk) => data += chunk);
        res.on('end', () => resolve(data.includes('Browser')));
      });
      req.on('error', () => resolve(false));
      req.setTimeout(2000, () => { req.destroy(); resolve(false); });
    });
  } catch { /* ignore */ }

  return { running, pids, hasCdp };
}

/**
 * Kill TradingView processes safely (does NOT kill Node.js/MCP server).
 * Uses targeted patterns to match only the Electron binary.
 */
async function killTradingView(platform) {
  try {
    if (platform === 'win32') {
      execSync('taskkill /F /IM TradingView.exe', { timeout: 5000 });
    } else if (platform === 'darwin') {
      // Kill only the TradingView Electron app and its Helper processes
      // Does NOT match Node.js processes running from tradingview-mcp directories
      execSync("pkill -f 'TradingView.app/Contents' 2>/dev/null || true", { timeout: 5000 });
    } else {
      // Linux: target known install paths
      execSync("pkill -f '/opt/TradingView/\\|/.local/share/TradingView/' 2>/dev/null || true", { timeout: 5000 });
    }
  } catch { /* may not be running */ }

  // Wait for processes to actually die (Electron needs time on macOS)
  for (let i = 0; i < 6; i++) {
    await new Promise(r => setTimeout(r, 500));
    const { running } = await detectRunningTV(9222);
    if (!running) return true;
  }
  // If still running after 3s, force kill
  try {
    if (platform !== 'win32') {
      execSync("pkill -9 -f 'TradingView.app/Contents' 2>/dev/null || true", { timeout: 3000 });
    }
  } catch { /* ignore */ }
  await new Promise(r => setTimeout(r, 1000));
  return true;
}

/**
 * Check if another process (not TradingView) is using the CDP port.
 */
async function checkPortConflict(cdpPort, platform) {
  try {
    if (platform === 'win32') {
      const out = execSync(`netstat -ano | findstr :${cdpPort} | findstr LISTENING`, { timeout: 3000 }).toString();
      if (out.trim()) return { conflict: true, detail: out.trim() };
    } else {
      const out = execSync(`lsof -i :${cdpPort} -sTCP:LISTEN 2>/dev/null || true`, { timeout: 3000 }).toString().trim();
      if (out && !out.includes('TradingView')) {
        return { conflict: true, detail: out };
      }
    }
  } catch { /* ignore */ }
  return { conflict: false };
}

export async function launch({ port, kill_existing } = {}) {
  const cdpPort = port || 9222;
  const killFirst = kill_existing !== false;
  const platform = process.platform;

  const pathMap = {
    darwin: [
      '/Applications/TradingView.app/Contents/MacOS/TradingView',
      `${process.env.HOME}/Applications/TradingView.app/Contents/MacOS/TradingView`,
    ],
    win32: [
      `${process.env.LOCALAPPDATA}\\TradingView\\TradingView.exe`,
      `${process.env.PROGRAMFILES}\\TradingView\\TradingView.exe`,
      `${process.env['PROGRAMFILES(X86)']}\\TradingView\\TradingView.exe`,
    ],
    linux: [
      '/opt/TradingView/tradingview',
      '/opt/TradingView/TradingView',
      `${process.env.HOME}/.local/share/TradingView/TradingView`,
      '/usr/bin/tradingview',
      '/snap/tradingview/current/tradingview',
    ],
  };

  let tvPath = null;
  const candidates = pathMap[platform] || pathMap.linux;
  for (const p of candidates) {
    if (p && existsSync(p)) { tvPath = p; break; }
  }

  if (!tvPath) {
    try {
      const cmd = platform === 'win32' ? 'where TradingView.exe' : 'which tradingview';
      tvPath = execSync(cmd, { timeout: 3000 }).toString().trim().split('\n')[0];
      if (tvPath && !existsSync(tvPath)) tvPath = null;
    } catch { /* ignore */ }
  }

  if (!tvPath && platform === 'darwin') {
    try {
      const found = execSync('mdfind "kMDItemFSName == TradingView.app" | head -1', { timeout: 5000 }).toString().trim();
      if (found) {
        const candidate = `${found}/Contents/MacOS/TradingView`;
        if (existsSync(candidate)) tvPath = candidate;
      }
    } catch { /* ignore */ }
  }

  if (!tvPath) {
    throw new Error(`TradingView not found on ${platform}. Searched: ${candidates.join(', ')}. Launch manually with: /path/to/TradingView --remote-debugging-port=${cdpPort}`);
  }

  // --- Check port conflict before doing anything ---
  const portCheck = await checkPortConflict(cdpPort, platform);
  if (portCheck.conflict) {
    throw new Error(`Port ${cdpPort} is already in use by another process (not TradingView). Free it first.\nDetail: ${portCheck.detail}`);
  }

  // --- Detect if TradingView is already running ---
  const detection = await detectRunningTV(cdpPort);

  if (detection.running && detection.hasCdp) {
    // Already running WITH CDP — just return success
    return {
      success: true, platform, binary: tvPath, cdp_port: cdpPort,
      cdp_url: `http://localhost:${cdpPort}`,
      note: 'TradingView already running with CDP enabled. No restart needed.',
      pids: detection.pids,
    };
  }

  if (detection.running && !detection.hasCdp) {
    // Running WITHOUT CDP — this is the critical case
    if (!killFirst) {
      // User said don't kill, but we can't add CDP to a running Electron app
      // Auto-escalate: kill and restart (the only way to fix this)
      const warning = 'TradingView is running WITHOUT CDP (--remote-debugging-port). ' +
        'Electron apps are single-instance — cannot add CDP to a running app. ' +
        'Auto-restarting with CDP enabled...';
      await killTradingView(platform);
      // Fall through to spawn below, but include the warning
      var autoEscalated = warning;
    } else {
      await killTradingView(platform);
    }
  } else if (killFirst && detection.running) {
    await killTradingView(platform);
  }

  // --- Spawn TradingView with CDP ---
  const child = spawn(tvPath, [`--remote-debugging-port=${cdpPort}`], { detached: true, stdio: 'ignore' });
  child.unref();

  // --- Wait for CDP with better diagnostics ---
  const http = await import('http');
  for (let i = 0; i < 20; i++) {
    await new Promise(r => setTimeout(r, 1000));
    try {
      const ready = await new Promise((resolve) => {
        const req = http.get(`http://localhost:${cdpPort}/json/version`, (res) => {
          let data = '';
          res.on('data', (chunk) => data += chunk);
          res.on('end', () => resolve(data));
        });
        req.on('error', () => resolve(null));
        req.setTimeout(3000, () => { req.destroy(); resolve(null); });
      });
      if (ready) {
        const info = JSON.parse(ready);
        const result = {
          success: true, platform, binary: tvPath, pid: child.pid,
          cdp_port: cdpPort, cdp_url: `http://localhost:${cdpPort}`,
          browser: info.Browser, user_agent: info['User-Agent'],
        };
        if (autoEscalated) result.warning = autoEscalated;
        return result;
      }
    } catch { /* retry */ }
  }

  // --- CDP still not ready — gather diagnostics ---
  const postDetection = await detectRunningTV(cdpPort);
  const diagnostics = {
    tv_process_alive: postDetection.running,
    tv_pids: postDetection.pids,
    cdp_responding: postDetection.hasCdp,
    spawned_pid: child.pid,
    spawned_pid_alive: false,
  };
  try {
    process.kill(child.pid, 0); // Check if spawned process is alive (signal 0 = test only)
    diagnostics.spawned_pid_alive = true;
  } catch { /* process died */ }

  return {
    success: false, platform, binary: tvPath, pid: child.pid, cdp_port: cdpPort, cdp_ready: false,
    warning: 'TradingView launched but CDP not responding after 20s.',
    diagnostics,
    hint: diagnostics.spawned_pid_alive
      ? 'TradingView is running but CDP never started. Check if another TradingView instance grabbed the singleton lock.'
      : 'The spawned TradingView process died. Check system logs or launch manually: ' + tvPath + ' --remote-debugging-port=' + cdpPort,
  };
}
