import fs from 'fs';
import path from 'path';

const ROOT_DIR = path.resolve(process.cwd());
const CLIPPINGS_DIR = path.join(ROOT_DIR, 'raw', 'clippings');
const LIBRARY_FILE = path.join(ROOT_DIR, 'wiki', 'library.md');
const INDEX_FILE = path.join(ROOT_DIR, 'wiki', 'index.md');

function run() {
  if (!fs.existsSync(CLIPPINGS_DIR)) {
    console.error('Clippings directory not found.');
    return;
  }

  const entries = fs.readdirSync(CLIPPINGS_DIR, { withFileTypes: true });
  const clippings = entries
    .filter(e => e.isFile() && e.name.endsWith('.md'))
    .map(e => e.name.replace('.md', ''))
    .sort();

  console.log(`Found ${clippings.length} clippings.`);

  let libraryContent = `# Biblioteca de Recortes (Clippings)\n\n`;
  libraryContent += `> Auto-gerado para indexar todos os artigos salvos pelo Web Clipper no Cofre do Obsidian ignorando nós órfãos.\n\n`;
  
  libraryContent += `## Índice Completo\n\n`;
  for (const clip of clippings) {
    libraryContent += `- [[${clip}]]\n`;
  }

  fs.writeFileSync(LIBRARY_FILE, libraryContent, 'utf-8');
  console.log(`Created ${LIBRARY_FILE} with ${clippings.length} links.`);

  // Update wiki/index.md to link to library
  let indexContent = fs.readFileSync(INDEX_FILE, 'utf-8');
  if (!indexContent.includes('[[library]]')) {
    // Add to Research / Indicadores Externos section
    indexContent = indexContent.replace(
      '## Research / Indicadores Externos',
      '## Research / Indicadores Externos\n- **[[library]]** — Índice mestre de todos os artigos capturados'
    );
    fs.writeFileSync(INDEX_FILE, indexContent, 'utf-8');
    console.log('Updated wiki/index.md with [[library]] reference.');
  }
}

run();
