from threading import Thread
import threading
from sequnce import action

print("Hello main")
thread = threading.Thread(target=action, args=())
thread.daemon = True                            # Daemonize thread
thread.start()
print("end of main")
