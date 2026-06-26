import os
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import metrics_engine as me  # noqa: E402

OUTPUT_DIR = os.path.join(me.BASE_DIR, 'wiki', 'outputs', 'charts')
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'accuracy-curve.png')

os.makedirs(OUTPUT_DIR, exist_ok=True)

# win → +1, loss → -1, open/expired → 0 (ignoradas no net score)
_SCORE = {'win': 1, 'loss': -1}

def parse_predictions():
    """Reusa o parser de metrics_engine; devolve (dates, statuses) ordenados por data."""
    records = sorted(me.parse_predictions(), key=lambda r: r['date'])
    dates = [r['date'] for r in records]
    statuses = [_SCORE.get(r['status'], 0) for r in records]
    return dates, statuses

def plot_accuracy():
    dates, statuses = parse_predictions()

    if not dates:
        print("Nenhuma previsão encontrada para plotar no log.")
        return

    # Calculate cumulative score
    scores = []
    current = 0
    for s in statuses:
        if s != 0: # Ignora empatadas/abertas pro equity
            current += s
        scores.append(current)

    # Plot
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot curve
    ax.plot(dates, scores, color='#00ff88', marker='o', linewidth=2, markersize=6)

    # Fill under curve correctly
    ax.fill_between(dates, 0, scores, where=[s >= 0 for s in scores], color='#00ff88', alpha=0.3)
    ax.fill_between(dates, 0, scores, where=[s < 0 for s in scores], color='#ff4444', alpha=0.3)

    # Format axes
    ax.set_title('Curva de Acurácia de Previsões (Net Score)', fontsize=14, pad=20, color='#ffffff')
    ax.set_ylabel('Net Score (Acertos - Erros)', color='#aaaaaa')
    ax.axhline(0, color='#aaaaaa', linewidth=1, linestyle='--')

    # Format x-axis dates
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=45)

    # Remove borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#555555')
    ax.spines['bottom'].set_color('#555555')

    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Curva de acurácia gerada com sucesso em: {OUTPUT_FILE}")

if __name__ == "__main__":
    plot_accuracy()
