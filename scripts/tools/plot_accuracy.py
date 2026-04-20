import os
import re
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Setup paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOG_FILE = os.path.join(BASE_DIR, 'wiki', 'brain', 'predictions-log.md')
OUTPUT_DIR = os.path.join(BASE_DIR, 'wiki', 'outputs', 'charts')
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'accuracy-curve.png')

os.makedirs(OUTPUT_DIR, exist_ok=True)

def parse_predictions():
    dates = []
    statuses = []
    
    if not os.path.exists(LOG_FILE):
        return dates, statuses

    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match blocks
    # ### [YYYY-MM-DD HH:MM] ... and find the Status line
    pattern = re.compile(
        r'### \[(\d{4}-\d{2}-\d{2})\s+\d{2}:\d{2}\].*?(?=- \*\*Status:\*\*).*?- \*\*Status:\*\* (⏳ aberta|✅ acertou|❌ errou|⚪ expirou)',
        re.DOTALL
    )
    
    for match in pattern.finditer(content):
        date_str = match.group(1)
        status_raw = match.group(2)
        
        try:
            dt = datetime.strptime(date_str, '%Y-%m-%d')
            dates.append(dt)
            
            if 'acertou' in status_raw:
                statuses.append(1)
            elif 'errou' in status_raw:
                statuses.append(-1)
            else:
                statuses.append(0) # aberta ou expirou
        except ValueError:
            pass
            
    # Sort by date
    combined = sorted(zip(dates, statuses), key=lambda x: x[0])
    if combined:
        dates, statuses = zip(*combined)
    else:
        dates, statuses = [], []
        
    return list(dates), list(statuses)

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
