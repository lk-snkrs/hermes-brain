#!/usr/bin/env python3
"""
Hermes Consolidation Weekly — Unificado
Executa: Learning Loop + Memory Consolidation + Knowledge Freshness Review
Rodar: Seg 9h
"""

import subprocess
import sys
import json
from datetime import datetime

LOG_PREFIX = "[Hermes Weekly Consolidation]"

def run_script(name, path):
    print(f"{LOG_PREFIX} Executando: {name}")
    try:
        result = subprocess.run(
            ["python3", path],
            capture_output=True,
            text=True,
            timeout=300
        )
        if result.returncode == 0:
            print(f"{LOG_PREFIX} ✓ {name} OK")
            return True
        else:
            print(f"{LOG_PREFIX} ✗ {name} ERRO: {result.stderr[:200]}")
            return False
    except Exception as e:
        print(f"{LOG_PREFIX} ✗ {name} EXCEPTION: {e}")
        return False

def main():
    print(f"{LOG_PREFIX} Iniciando — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    results = []
    
    # 1. Learning Loop
    results.append(run_script("Learning Loop", "/root/.hermes/scripts/hermes_learning_loop.py"))
    
    # 2. Knowledge Freshness Review
    results.append(run_script("Knowledge Freshness", "/root/.hermes/scripts/hermes_knowledge_freshness.py"))
    
    # 3. Learning Review
    results.append(run_script("Learning Review", "/root/.hermes/scripts/hermes_learning_review.py"))
    
    print(f"{LOG_PREFIX} Finalizado — Sucessos: {sum(results)}/3")

if __name__ == "__main__":
    main()
