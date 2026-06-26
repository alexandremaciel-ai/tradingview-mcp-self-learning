import { z } from 'zod';
import { handle } from './_format.js';
import * as core from '../core/tab.js';

export function registerTabTools(server) {
  server.tool('tab_list', 'List all open TradingView chart tabs', {}, handle(core.list));

  server.tool('tab_new', 'Open a new chart tab', {}, handle(core.newTab));

  server.tool('tab_close', 'Close the current chart tab', {}, handle(core.closeTab));

  server.tool('tab_switch', 'Switch to a chart tab by index', {
    index: z.coerce.number().describe('Tab index (0-based, from tab_list)'),
  }, handle(core.switchTab));
}
