import psutil
import time
import logging

# ================== CONFIGURATION ==================
THRESHOLD = 80          # CPU usage alert threshold (%)
CHECK_INTERVAL = 1      # Check interval in seconds
LOG_FILE = "cpu_monitor.log"
# ===================================================

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def monitor_cpu(threshold=THRESHOLD, interval=CHECK_INTERVAL):
    print("Monitoring CPU usage... (Press Ctrl+C to stop)\n")

    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=interval)

            if cpu_usage > threshold:
                alert_msg = f"⚠️ Alert! CPU usage exceeds threshold: {cpu_usage}%"
                print(alert_msg)
                logging.warning(alert_msg)
            else:
                logging.info(f"CPU usage: {cpu_usage}%")

            # Optional small delay to prevent unnecessary overhead
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n✅ Monitoring stopped by user.")
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"❌ Error occurred: {e}")

if __name__ == "__main__":
    monitor_cpu()

