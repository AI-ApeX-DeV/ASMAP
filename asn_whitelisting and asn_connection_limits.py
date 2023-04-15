# Define a list of whitelisted ASNs
whitelisted_asns = [12345, 67890]

# Define a dictionary to store connection limits for specific ASNs
asn_connection_limits = {12345: 10, 67890: 5}

# Define a dictionary to store the current number of connections for each ASN
asn_connections = {}

# Function to check if a peer is associated with a whitelisted ASN
def is_whitelisted(peer):
    if peer.asn in whitelisted_asns:
        return True
    else:
        return False

# Function to check if a peer is allowed to connect based on their ASN
def can_connect(peer):
    # Check if the peer's ASN is whitelisted
    if not is_whitelisted(peer):
        return False
    
    # Get the connection limit for the peer's ASN
    connection_limit = asn_connection_limits.get(peer.asn, float('inf'))
    
    # Get the current number of connections for the peer's ASN
    current_connections = asn_connections.get(peer.asn, 0)
    
    # Check if the connection limit has been reached
    if current_connections >= connection_limit:
        return False
    
    # The peer is allowed to connect
    return True

# Function to handle incoming connections from peers
def handle_incoming_connection(peer):
    if can_connect(peer):
        # Accept the connection
        peer.accept()
        
        # Update the number of connections for the peer's ASN
        asn_connections[peer.asn] = asn_connections.get(peer.asn, 0) + 1
    else:
        # Reject the connection
        peer.reject()