#This file is designed to run the host of experiments that I layed out in the description. I did use the help of gpt to 
#write this chunk of code and ensure things ran smoothly! I did not use combinations of different losses and the novel score
#function I introduced in my modification. 
import subprocess, time, re, pandas as pd

experiments = [
    ("baseline", 0.00, None, None),
    ("progress_lam_025", 0.25, None, None),
    ("progress_lam_050", 0.50, None, None),
    ("pre_loss_25", 0.00, "loss", 0.25),
    ("pre_logloss_25", 0.00, "log_loss", 0.25),
    ("pre_confidence_25", 0.00, "confidence", 0.25),
    ("pre_margin_25", 0.00, "margin", 0.25),
]

rows = []

for name, progress_lam, score_strategy, top_fraction in experiments:
    print("\n" + "=" * 80)
    print(f"Running: {name}")

    code = f"""
import Adaptive_Auto_Attack_main as aaa
aaa.main(
    'AAA',
    model_name='TRADES_mnist',
    average_number=1000,
    progress_lam={progress_lam},
    score_strategy={repr(score_strategy)},
    top_fraction={repr(top_fraction)}
)
"""

    start = time.time()
    result = subprocess.run(["python", "-c", code], capture_output=True, text=True)
    elapsed = time.time() - start
    output = result.stdout + result.stderr

    clean_matches = re.findall(r"clean_acc:\s*([0-9.]+)|clean acc:\s*([0-9.]+)", output)
    robust_matches = re.findall(r"robust acc:\s*([0-9.]+)", output)

    clean_vals = [a or b for a, b in clean_matches]

    rows.append({
        "experiment": name,
        "progress_lam": progress_lam,
        "score_strategy": score_strategy,
        "top_fraction": top_fraction,
        "status": "ok" if result.returncode == 0 else "error",
        "clean_acc_last": float(clean_vals[-1]) if clean_vals else None,
        "robust_acc_last": float(robust_matches[-1]) if robust_matches else None,
        "wall_clock_sec": round(elapsed, 2),
    })

df = pd.DataFrame(rows)
df.to_csv("experiment_results.csv", index=False)

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

print("\nFinal Results:\n")
print(df.to_string(index=False))
print("\nSaved results to experiment_results.csv")

try:
    from IPython.display import display
    display(df)
except Exception:
    pass
