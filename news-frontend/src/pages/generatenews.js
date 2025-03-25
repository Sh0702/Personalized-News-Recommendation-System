import React, { useState } from 'react';
import API from '../api';

function GenerateNews() {
  const [query, setQuery] = useState('');
  const [result, setResult] = useState('');

  const fetchNews = async () => {
    try {
      const res = await API.post('/generate_news', { query });
      setResult(res.data);
    } catch (err) {
      alert('News generation failed');
    }
  };

  return (
    <div>
      <h2>Personalized News Generator</h2>
      <input placeholder="Enter your query..." onChange={e => setQuery(e.target.value)} />
      <button onClick={fetchNews}>Generate</button>
      {result && (
        <div>
          <h3>Summary</h3>
          <p>{result.summary}</p>
          <h4>Explanation</h4>
          <p>{result.explanation}</p>
        </div>
      )}
    </div>
  );
}

export default GenerateNews;
