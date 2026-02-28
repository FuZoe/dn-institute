#!/usr/bin/env python3
"""Patch enriched_bounties.json with expert Hunter Intelligence"""

import json
import re

INPUT_FILE = "bounty_issues.json"
OUTPUT_FILE = "enriched_bounties.json"

EXPERT_INTEL = {
    819: {
        "friction_level": "High",
        "technical_hint": "S-Tier Target. Investigative work needed on the auto scan-mode concurrency loop. Suspected unclosed channels or goroutine leak after 25k+ targets. Check sync.WaitGroup implementation."
    },
    6398: {
        "friction_level": "Low",
        "technical_hint": "REGRESSION detected. Path-based fuzzing skips numeric segments. Compare pkg/protocols/http/fuzzing between v3.4.7 and v3.4.8 to identify the breaking commit."
    },
    6674: {
        "friction_level": "Low",
        "technical_hint": "Straightforward fix. Replace panic with fmt.Errorf in pkg/catalog/loader/loader.go and propagate errors to lazy.go. Good for quick payout."
    },
    6403: {
        "friction_level": "Medium",
        "technical_hint": "Strategic Enhancement. Design a 'Control Template' check to detect honeypots that return 200 OK for all patterns. Focus on fingerprinting 'False Positive' behavior."
    },
    1367: {
        "friction_level": "Medium",
        "technical_hint": "CGO Elimination. Target is to replace smacker/go-tree-sitter with a pure Go alternative (e.g., modernc.org/cc) to unblock darwin/arm64 cross-compilation."
    },
    2240: {
        "friction_level": "High",
        "technical_hint": "Protocol Conflict. Inject a DisableHTTP2 option into the retryablehttp-go transport layer to honor the -pr http11 flag. Watch out for overlapping PRs."
    },
    1434: {
        "friction_level": "Medium",
        "technical_hint": "Rate-limiting bug. Re-evaluate the rl, rls options for sitedossier source. Check if c3d8a02 commit logic needs to be ported to current version."
    },
    6592: {
        "friction_level": "Medium",
        "technical_hint": "Race condition in authenticated scanning. The secret-file template needs to complete before other templates start. Check template execution ordering in runner."
    },
    6532: {
        "friction_level": "Low",
        "technical_hint": "CI Integration task. Add typos GitHub Action to .github/workflows. Reference existing CI patterns and typos documentation."
    },
    5838: {
        "friction_level": "High",
        "technical_hint": "Complex feature. Build XSS context analyzer to detect injection points in HTML/JS/attribute contexts. Consider using HTML parser and state machine approach."
    },
    5567: {
        "friction_level": "Medium",
        "technical_hint": "Config improvement. Extend goflags to support embedded file content and ignore extra YAML fields in template profiles."
    },
    2063: {
        "friction_level": "Low",
        "technical_hint": "PDF export feature. Use a Go PDF library (e.g., gofpdf) to convert scan results to formatted PDF reports."
    },
    924: {
        "friction_level": "Medium",
        "technical_hint": "Wildcard detection. Implement puredns-style auto wildcard discovery using random subdomain probing and response fingerprinting."
    },
    611: {
        "friction_level": "Medium",
        "technical_hint": "Headless mode timeout. Debug DOM acquisition in hybrid crawler mode. Check chromedp context timeout settings."
    },
    859: {
        "friction_level": "Low",
        "technical_hint": "Input parsing bug. Add comma-separated prefix splitting in the -l/-list option handler, similar to -u option behavior."
    }
}

def get_bounty_amount(labels):
    for label in labels:
        if label.startswith("$"):
            amount_str = label[1:].lower().replace(",", "")
            if "k" in amount_str:
                return int(float(amount_str.replace("k", "")) * 1000)
            try:
                return int(float(amount_str))
            except ValueError:
                continue
    return 0

def get_bounty_tier(amount):
    if amount >= 500:
        return "S-Tier"
    elif amount >= 200:
        return "A-Tier"
    return "B-Tier"

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        issues = json.load(f)
    
    enriched = []
    for issue in issues:
        num = issue["number"]
        amount = get_bounty_amount(issue["labels"])
        tier = get_bounty_tier(amount)
        
        if num in EXPERT_INTEL:
            intel = EXPERT_INTEL[num]
        else:
            intel = {
                "friction_level": "Medium",
                "technical_hint": "Standard Bugfix: Review issue description for environment reproduction steps."
            }
        
        enriched.append({
            **issue,
            "hunter_intelligence": {
                "friction_level": intel["friction_level"],
                "technical_hint": intel["technical_hint"],
                "bounty_tier": tier,
                "bounty_amount": amount
            }
        })
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(enriched, f, indent=2, ensure_ascii=False)
    
    print(f"Patched {len(enriched)} issues with expert intelligence")
    print(f"Output: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
