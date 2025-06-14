## Listing Devices
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

fontsize = 24
linewidth = 2

def extract_columns_from_csv(file_path, columns):
    df = pd.read_csv(file_path)
    extracted_data = df[columns]
    return extracted_data

# Listing devices on the network 
def listing_devices():
    file_path = 'graphs/listing-devices.csv'
    data = extract_columns_from_csv(file_path, ['Devices', 'TAv', 'SD', 'DB Size'])
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # Plotting TAv with standard deviation
    ax1.errorbar(data['Devices'], data['TAv'], yerr=data['SD'], fmt='-o', label='Average Response Time', color='b', linewidth=linewidth)
    ax1.set_ylabel('Average Time (ms)', fontsize=fontsize)
    ax1.tick_params(axis='y', labelsize=fontsize)
    ax1.set_xticks([])
    ax1.set_title('Number of Devices vs Average Time', fontsize=fontsize)
    ax1.legend(loc="upper left", fontsize=fontsize)

    # Plotting DB Size
    ax2.plot(data['Devices'], data['DB Size'], 'o--', label='DB Size', color='crimson', linewidth=linewidth)
    ax2.set_xlabel('Number of Devices', fontsize=fontsize)
    ax2.set_ylabel('Database Size (Bytes)', fontsize=fontsize)
    ax2.tick_params(axis='y', labelsize=fontsize)
    ax2.set_xticks(range(0, max(data['Devices']) + 1, 10))
    ax2.tick_params(axis='x', labelsize=fontsize)
    # ax2.set_title('Number of Devices vs Database Size', fontsize=fontsize)
    ax2.legend(loc="upper left", fontsize=fontsize)

    fig.tight_layout()
    with PdfPages('graphs/listing-devices.pdf') as pdf:
        pdf.savefig(fig)
    plt.close(fig)

# Applying a policy to a device
def applying_policy():
    file_path = 'graphs/applying-policy.csv'
    data = extract_columns_from_csv(file_path, ['Policies', 'TAv', 'SD', 'MUD File Size'])
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # Plotting TAv with standard deviation
    ax1.errorbar(data['Policies'], data['TAv'], yerr=data['SD'], fmt='-o', label='Average Response Time', color='b', linewidth=linewidth)
    ax1.set_ylabel('Average Time (ms)', fontsize=fontsize)
    ax1.tick_params(axis='y', labelsize=fontsize)
    ax1.set_xticks([])
    ax1.set_title('Number of Policies vs Average Time', fontsize=fontsize)
    ax1.legend(loc="upper left", fontsize=fontsize)

    # Plotting MUD File Size
    ax2.plot(data['Policies'], data['MUD File Size'], 'o--', label='MUD File Size', color='crimson', linewidth=linewidth)
    ax2.set_xlabel('Number of Policies', fontsize=fontsize)
    ax2.set_ylabel('MUD File Size (Bytes)', fontsize=fontsize)
    ax2.tick_params(axis='y', labelsize=fontsize)
    ax2.set_xticks([2, 20, 40])
    ax2.tick_params(axis='x', labelsize=fontsize)
    # ax2.set_title('Number of Policies vs MUD File Size', fontsize=fontsize)
    ax2.legend(loc="upper left", fontsize=fontsize)

    fig.tight_layout()
    with PdfPages('graphs/applying-policy.pdf') as pdf:
        pdf.savefig(fig)
    plt.close(fig)
    
# Loading MUD file for a device
def active_mudfiles():
    file_path = 'graphs/active-mudfiles.csv'
    data = extract_columns_from_csv(file_path, ['Policies', 'TAv', 'SD', 'MUD File Size'])
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # Plotting TAv with standard deviation
    ax1.errorbar(data['Policies'], data['TAv'], yerr=data['SD'], fmt='-o', label='Average Response Time', color='b', linewidth=linewidth)
    ax1.set_ylabel('Average Time (ms)', fontsize=fontsize)
    ax1.tick_params(axis='y', labelsize=fontsize)
    ax1.set_xticks([])
    ax1.set_title('Number of Policies vs Average Time', fontsize=fontsize)
    ax1.legend(loc="upper left", fontsize=fontsize)
    
    # Plotting MUD File Size
    ax2.plot(data['Policies'], data['MUD File Size'], 'o--', label='MUD File Size', color='crimson', linewidth=linewidth)
    ax2.set_xlabel('Number of Policies', fontsize=fontsize)
    ax2.set_ylabel('MUD File Size (Bytes)', fontsize=fontsize)
    ax2.tick_params(axis='y', labelsize=fontsize)
    ax2.set_xticks([2, 20, 40])
    ax2.tick_params(axis='x', labelsize=fontsize)
    # ax2.set_title('Number of Policies vs MUD File Size', fontsize=fontsize)
    ax2.legend(loc="upper left", fontsize=fontsize)

    fig.tight_layout()
    with PdfPages('graphs/active-mudfiles.pdf') as pdf:
        pdf.savefig(fig)
    plt.close(fig)

listing_devices()
applying_policy()
active_mudfiles()