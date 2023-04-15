# Define a list of blacklisted ASNs
blacklisted_asns = [12345, 67890]

# Define a dictionary to store ban durations for specific ASNs
asn_ban_durations = {12345: 3600, 67890: 86400}

# Function to check if a peer is associated with a blacklisted ASN
def is_blacklisted(peer):
    if peer.asn in blacklisted_asns:
        return True
    else:
        return False

# Function to ban a peer based on their ASN
def ban_peer(peer):
    if is_blacklisted(peer):
        # Get the ban duration for the peer's ASN
        ban_duration = asn_ban_durations.get(peer.asn, 0)
        
        # Ban the peer for the specified duration
        peer.ban(ban_duration)