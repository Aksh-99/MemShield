import shap
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

#Load model
with open('memshield_model.pkl', 'rb') as f:
    bundle = pickle.load(f)

model = bundle['model']
scaler = bundle['scaler']

#Load Dataset
df = pd.read_csv('Obfuscated-MalMem2022.csv')
feature_names = df.drop(['Category', 'Class'], axis=1).columns.tolist()
X_scaled = scaler.transform(df.drop(['Category', 'Class'], axis=1).values)

#Explainer
explainer = shap.LinearExplainer(model, X_scaled)
shap_values = explainer(X_scaled)

#Visualization
rename_map = {
    'svcscan.process_services': 'Process Services',
    'pslist.avg_threads': 'Average Threads',
    'handles.nmutant': 'Mutant Handles',
    'svcscan.nservices': 'Number of Services',
    'svcscan.shared_process_services': 'Shared Process Services',
    'pslist.nppid': 'Parent Process ID Count',
    'handles.nevent': 'Event Handles',
    'dlllist.avg_dlls_per_proc': 'Average DLLs per Process',
    'modules.nmodules': 'Loaded Modules',
    'ldrmodules.not_in_load': 'Modules Not Loaded',
    'ldrmodules.not_in_mem': 'Modules Missing from Memory',
    'handles.nthread': 'Thread Handles',
    'svcscan.nactive': 'Active Services',
    'ldrmodules.not_in_init': 'Modules Not Initialized',
    'psxview.not_in_deskthrd_false_avg': 'Hidden Desktop Threads',
    'dlllist.ndlls': 'Number of DLLs',
    'handles.ntimer': 'Timer Handles',
    'psxview.not_in_csrss_handles_false_avg': 'Hidden CSRSS Handles',
    'handles.nsemaphore': 'Semaphore Handles',
    'psxview.not_in_ethread_pool_false_avg': 'Hidden EThread Pool Objects'
}
feature_names_clean = [rename_map.get(f, f) for f in feature_names]
shap.summary_plot(shap_values, X_scaled, feature_names=feature_names_clean, show=False)
plt.savefig('shap_summary.png', bbox_inches='tight')
print("Saved to shap_summary.png")