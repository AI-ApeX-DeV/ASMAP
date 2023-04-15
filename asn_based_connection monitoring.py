# Define a dictionary to store connection metrics for each ASN
asn_metrics = {}

# Function to update connection metrics for a peer
def update_metrics(peer):
    # Get the peer's ASN
    asn = peer.asn
    
    # Initialize metrics for the ASN if they don't exist
    if asn not in asn_metrics:
        asn_metrics[asn] = {
            'connections': 0,
            'data_transferred': 0,
            'failed_connections': 0,
            'invalid_transactions': 0
        }
    
    # Update the metrics
    asn_metrics[asn]['connections'] += 1
    asn_metrics[asn]['data_transferred'] += peer.data_transferred
    if not peer.connection_successful:
        asn_metrics[asn]['failed_connections'] += 1
    asn_metrics[asn]['invalid_transactions'] += peer.invalid_transactions

# Function to monitor connection metrics for an ASN
def monitor_asn(asn):
    # Get the metrics for the ASN
    metrics = asn_metrics.get(asn, None)
    
    # Check if any unusual activity is detected
    if metrics:
        if metrics['failed_connections'] > 10:
            print(f'Warning: High number of failed connections for ASN {asn}')
        if metrics['invalid_transactions'] > 5:
            print(f'Warning: High number of invalid transactions for ASN {asn}')