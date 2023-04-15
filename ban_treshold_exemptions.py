# Define a dictionary to store ban thresholds for specific ASNs
asn_ban_thresholds = {12345: {'failed_connections': 5, 'invalid_transactions': 3}}

# Define a set to store exempted peers
exempted_peers = set()

# Function to check if a peer should be banned based on their ASN
def should_ban(peer):
    # Check if the peer is exempted from bans
    if peer in exempted_peers:
        return False
    
    # Get the ban thresholds for the peer's ASN
    thresholds = asn_ban_thresholds.get(peer.asn, {})
    
    # Check if any thresholds are exceeded
    if peer.failed_connections > thresholds.get('failed_connections', float('inf')):
        return True
    if peer.invalid_transactions > thresholds.get('invalid_transactions', float('inf')):
        return True
    
    # The peer should not be banned
    return False

# Function to ban a peer based on their ASN
def ban_peer(peer):
    if should_ban(peer):
        # Ban the peer
        peer.ban()