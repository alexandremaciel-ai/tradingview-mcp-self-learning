import fs from 'fs';
import path from 'path';

// Localize relative to project root
const ROOT_DIR = path.resolve(process.cwd());
const WIKI_DIR = path.join(ROOT_DIR, 'wiki');
const CLIPPINGS_DIR = path.join(ROOT_DIR, 'raw', 'clippings');

function getAllMarkdownFiles(dirPath, files = []) {
  if (!fs.existsSync(dirPath)) return files;
  
  const entries = fs.readdirSync(dirPath, { withFileTypes: true });
  for (const entry of entries) {
    if (entry.name.startsWith('.') || entry.name === 'outputs' || entry.name === 'lint') continue;
    
    const fullPath = path.join(dirPath, entry.name);
    if (entry.isDirectory()) {
      getAllMarkdownFiles(fullPath, files);
    } else if (fullPath.endsWith('.md')) {
      files.push(fullPath);
    }
  }
  return files;
}

export async function searchWiki(query, limit = 10) {
  const queryLower = query.toLowerCase();
  const searchTerms = queryLower.split(/\s+/).filter(w => w.length > 2);
  
  if (searchTerms.length === 0) {
    throw new Error('Search query must contain words longer than 2 characters.');
  }

  const allFiles = [
    ...getAllMarkdownFiles(WIKI_DIR),
    ...getAllMarkdownFiles(CLIPPINGS_DIR)
  ];

  const results = [];

  for (const file of allFiles) {
    const content = fs.readFileSync(file, 'utf8');
    const contentLower = content.toLowerCase();
    
    let score = 0;
    let mainMatchIndex = -1;

    // Exact full query match
    if (contentLower.includes(queryLower)) {
      score += 10;
      mainMatchIndex = contentLower.indexOf(queryLower);
    }

    // Individual term match
    for (const term of searchTerms) {
      const regex = new RegExp(term, 'gi');
      const matches = content.match(regex);
      if (matches) {
        score += matches.length;
        if (mainMatchIndex === -1) mainMatchIndex = contentLower.indexOf(term);
      }
    }

    if (score > 0) {
      // Create a snippet around the match
      let snippet = '';
      if (mainMatchIndex !== -1) {
        const start = Math.max(0, mainMatchIndex - 40);
        const end = Math.min(content.length, mainMatchIndex + query.length + 80);
        snippet = `...${content.slice(start, end).replace(/\n/g, ' ')}...`;
      }
      
      const relativePath = path.relative(ROOT_DIR, file);
      results.push({ path: relativePath, score, snippet });
    }
  }

  results.sort((a, b) => b.score - a.score);
  return {
    query,
    results_found: results.length,
    top_matches: results.slice(0, limit)
  };
}
