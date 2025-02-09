try:
    from pox.core import core
    import pox.openflow.libopenflow_01 as of
except ModuleNotFoundError:
    raise ImportError("POX module not found. Ensure POX is installed and properly configured in your environment.")

import threading
import time
import collections

log = core.getLogger()

# Threshold values for anomaly detection
THRESHOLD_PACKET_RATE = 100  # Packets per second
THRESHOLD_BYTE_RATE = 1000000  # Bytes per second

# Data structure to store traffic statistics
flow_stats = collections.defaultdict(lambda: {'packets': 0, 'bytes': 0, 'timestamp': time.time()})

def detect_anomalies():
    """Thread to periodically check for anomalies in traffic."""
    while True:
        time.sleep(5)  # Monitor every 5 seconds
        current_time = time.time()
        for flow, stats in list(flow_stats.items()):
            time_diff = current_time - stats['timestamp']
            if time_diff > 0:
                packet_rate = stats['packets'] / time_diff
                byte_rate = stats['bytes'] / time_diff
                
                if packet_rate > THRESHOLD_PACKET_RATE or byte_rate > THRESHOLD_BYTE_RATE:
                    log.warning(f"Anomaly detected for flow {flow}: Packet Rate={packet_rate}, Byte Rate={byte_rate}")
                
                # Reset stats
                stats['packets'] = 0
                stats['bytes'] = 0
                stats['timestamp'] = current_time

class IDSController (object):
    def __init__(self):
        core.openflow.addListeners(self)
        threading.Thread(target=detect_anomalies, daemon=True).start()
        log.info("IDS Controller initialized")

    def _handle_PacketIn(self, event):
        """Handle incoming packets and update flow statistics."""
        packet = event.parsed
        if not packet:
            return
        
        src = packet.src
        dst = packet.dst
        flow_key = (src, dst)
        
        flow_stats[flow_key]['packets'] += 1
        flow_stats[flow_key]['bytes'] += len(event.data)
        flow_stats[flow_key]['timestamp'] = time.time()
        
        # Forward the packet normally
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(msg)

# Launch function for POX
def launch():
    core.registerNew(IDSController)
    log.info("IDS module for SDN started")
