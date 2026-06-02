#!/usr/bin/env python3
"""
plot_metrics.py — Gráficos de calibração e win rate a partir do brain.

Reaproveita o parser de metrics_engine.py e gera, em wiki/outputs/charts/:
  - calibration.png      → confiança prometida × win rate observado
  - winrate-by-side.png  → win rate por lado e por regime macro

Requer matplotlib (mesma dependência de plot_accuracy.py). Se ausente, o script
imprime instrução e sai sem erro (não quebra CI/automação).

Uso:
  python scripts/tools/plot_metrics.py
"""

import os
import sys

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, THIS_DIR)

import metrics_engine as me  # noqa: E402

OUTPUT_DIR = os.path.join(me.BASE_DIR, 'wiki', 'outputs', 'charts')


def main():
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print('matplotlib não instalado — pulei a geração de gráficos.')
        print('Instale com: pip install matplotlib')
        return

    records = me.parse_predictions()
    if not records:
        print('Nenhuma previsão encontrada.')
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plt.style.use('dark_background')

    # --- Gráfico 1: Calibração ---
    cal_rows, brier, n = me.calibration(records)
    levels, probs, obs = [], [], []
    for lvl, prob, w, l, wr in cal_rows:
        if wr is not None:
            levels.append(lvl)
            probs.append(prob * 100)
            obs.append(wr)

    if levels:
        fig, ax = plt.subplots(figsize=(8, 5))
        x = range(len(levels))
        width = 0.38
        ax.bar([i - width / 2 for i in x], probs, width, label='Prob. prometida', color='#5599ff')
        ax.bar([i + width / 2 for i in x], obs, width, label='Win rate observado', color='#00ff88')
        ax.set_xticks(list(x))
        ax.set_xticklabels(levels)
        ax.set_ylabel('%')
        title = 'Calibração de Confiança'
        if brier is not None:
            title += f' (Brier {brier:.3f}, n={n})'
        ax.set_title(title, color='#ffffff')
        ax.legend()
        ax.set_ylim(0, 105)
        plt.tight_layout()
        path1 = os.path.join(OUTPUT_DIR, 'calibration.png')
        plt.savefig(path1, dpi=150, bbox_inches='tight')
        plt.close()
        print('Gerado:', os.path.relpath(path1, me.BASE_DIR))

    # --- Gráfico 2: Win rate por lado e regime ---
    def wr_bars(keyfn):
        rows = me.group_table(records, keyfn, '')
        labels, vals = [], []
        for k, w, l, o, e, wr in rows:
            if wr is not None and (w + l) > 0:
                labels.append(k)
                vals.append(wr)
        return labels, vals

    side_labels, side_vals = wr_bars(lambda r: r['side'])
    reg_labels, reg_vals = wr_bars(lambda r: r['regime'])

    if side_labels or reg_labels:
        fig, axes = plt.subplots(1, 2, figsize=(11, 5))
        for ax, labels, vals, title in (
            (axes[0], side_labels, side_vals, 'Win Rate por Lado'),
            (axes[1], reg_labels, reg_vals, 'Win Rate por Regime'),
        ):
            ax.bar(labels, vals, color='#00ff88')
            ax.set_title(title, color='#ffffff')
            ax.set_ylabel('Win Rate %')
            ax.set_ylim(0, 105)
            ax.axhline(50, color='#aaaaaa', linewidth=1, linestyle='--')
        plt.tight_layout()
        path2 = os.path.join(OUTPUT_DIR, 'winrate-by-side.png')
        plt.savefig(path2, dpi=150, bbox_inches='tight')
        plt.close()
        print('Gerado:', os.path.relpath(path2, me.BASE_DIR))


if __name__ == '__main__':
    main()
