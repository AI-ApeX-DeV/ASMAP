# Define a list to store information on banned peers
banned_peers = []

# Function to ban a peer and record information on the ban
def ban_peer(peer, reason):
    # Ban the peer
    peer.ban()
    
    # Record information on the ban
    banned_peers.append({
        'peer': peer,
        'asn': peer.asn,
        'timestamp': time.time(),
        'reason': reason
    })

# Function to generate a report on banned peers
def generate_ban_report():
    # Group banned peers by ASN
    asn_groups = {}
    for ban in banned_peers:
        asn = ban['asn']
        if asn not in asn_groups:
            asn_groups[asn] = []
        asn_groups[asn].append(ban)
    
    # Generate the report
    report = []
    for asn, bans in asn_groups.items():
        report.append(f'ASN: {asn}')
        for ban in bans:
            timestamp = datetime.fromtimestamp(ban['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
            report.append(f'  - Peer: {ban["peer"]}, Timestamp: {timestamp}, Reason: {ban["reason"]}')
    
    return '\n'.join(report)