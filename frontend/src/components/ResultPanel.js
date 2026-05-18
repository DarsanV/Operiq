// components/ResultPanel.js
import React, { useState } from 'react';
import JSZip from 'jszip';
import { saveAs } from 'file-saver';

function ResultPanel({ result }) {
  const [activeTab, setActiveTab] = useState('plan');

  if (!result) return null;

  const handleDownload = () => {
    const zip = new JSZip();
    
    // Create root folder
    const folderName = result.task ? result.task.replace(/[^a-zA-Z0-9]/g, '_').toLowerCase().substring(0, 20) : 'project';
    const root = zip.folder(folderName);
    
    // Add Plan
    const planText = result.plan ? result.plan.map((step, i) => `${i + 1}. ${step}`).join('\n') : '';
    root.file("plan.txt", planText);
    
    // Add Docs as README.md
    root.file("README.md", result.documentation || "");

    // MVC Structure for Java code
    const srcFolder = root.folder("src").folder("main").folder("java").folder("com").folder("app");
    const modelFolder = srcFolder.folder("model");
    const controllerFolder = srcFolder.folder("controller");
    const serviceFolder = srcFolder.folder("service");
    
    // Split the backend code by 'class ' or '@' to rudimentarily place them in folders
    const code = result.backendCode || "";
    
    // A simple heuristic to put the code into the right folders if it's all one string
    if (code.includes("@RestController") || code.includes("Controller")) {
       controllerFolder.file("AppController.java", code);
    } else if (code.includes("@Service")) {
       serviceFolder.file("AppService.java", code);
    } else {
       // Just put everything in the main folder if we can't determine
       srcFolder.file("GeneratedApp.java", code);
    }
    
    // Create empty MVC folders just to ensure the structure exists
    modelFolder.file(".keep", "");
    controllerFolder.file(".keep", "");
    serviceFolder.file(".keep", "");

    zip.generateAsync({ type: "blob" }).then((content) => {
      saveAs(content, `${folderName}.zip`);
    });
  };

  return (
    <div className="result-panel tech-panel">
      <div className="result-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h3>EXECUTION COMPLETE <span className="task-id">ID:{result.taskId || result.id || 'NULL'}</span></h3>
          <p className="task-title">"{result.task}"</p>
        </div>
        <button className="primary-btn" onClick={handleDownload} style={{ padding: '0.5rem 1rem', fontSize: '0.9rem' }}>
          [↓] EXPORT_ZIP
        </button>
      </div>

      <div className="tabs">
        <button
          className={activeTab === 'plan' ? 'tab active' : 'tab'}
          onClick={() => setActiveTab('plan')}
        >
          // ARCHITECTURE
        </button>
        <button
          className={activeTab === 'code' ? 'tab active' : 'tab'}
          onClick={() => setActiveTab('code')}
        >
          // SOURCE_CODE
        </button>
        <button
          className={activeTab === 'docs' ? 'tab active' : 'tab'}
          onClick={() => setActiveTab('docs')}
        >
          // API_SPEC
        </button>
      </div>

      <div className="tab-content">
        {activeTab === 'plan' && (
          <div className="plan-content">
            <h4>SYS.PLANNER LOG:</h4>
            <ol>
              {result.plan && result.plan.map((step, i) => (
                <li key={i}>{step}</li>
              ))}
            </ol>
          </div>
        )}

        {activeTab === 'code' && (
          <div className="code-content">
            <h4>SYS.BACKEND OUTPUT:</h4>
            <pre><code>{result.backendCode}</code></pre>
          </div>
        )}

        {activeTab === 'docs' && (
          <div className="docs-content">
            <h4>SYS.DOCS OUTPUT:</h4>
            <pre className="docs-text">{result.documentation}</pre>
          </div>
        )}
      </div>
    </div>
  );
}

export default ResultPanel;
