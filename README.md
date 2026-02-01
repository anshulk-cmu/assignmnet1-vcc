# VirtualBox Microservice Deployment

A distributed microservice application deployed across three Virtual Machines using Oracle VirtualBox and FastAPI.

## 📋 Project Overview

This project demonstrates the creation and configuration of multiple VMs using VirtualBox, establishing network connectivity between them, and deploying a simple microservice-based application.

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        INTERNET                             │
└──────────────────────────┬──────────────────────────────────┘
                           │
                  NAT Gateway (10.0.2.1)
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
    ┌────┴────┐       ┌────┴────┐       ┌────┴────┐
    │   VM1   │       │   VM2   │       │   VM3   │
    │ Gateway │  -->  │Validator│  -->  │ Greeter │
    │10.0.2.3 │       │10.0.2.4 │       │10.0.2.5 │
    │  :8001  │       │  :8002  │       │  :8003  │
    └─────────┘       └─────────┘       └─────────┘
```

### Request Flow

1. **VM1 (API Gateway)** - Receives incoming requests and forwards to VM2
2. **VM2 (Validator)** - Validates the input data and forwards to VM3
3. **VM3 (Greeter)** - Generates and returns the final response

## 🖥️ VM Configuration

| VM | Hostname | IP Address | Port | Role |
|----|----------|------------|------|------|
| VM1 | vm1-api | 10.0.2.3 | 8001 | API Gateway |
| VM2 | vm2-validation | 10.0.2.4 | 8002 | Validator Service |
| VM3 | vm3-greeter | 10.0.2.5 | 8003 | Greeter Service |

### Hardware Specifications (Per VM)
- **RAM:** 4096 MB (4 GB)
- **CPU:** 2 Cores
- **Storage:** 64 GB (Dynamically Allocated)
- **OS:** Ubuntu Server 24.04.3 LTS
- **Network:** NAT Network (MicroserviceNetwork)

## 🚀 Installation & Setup

### Prerequisites
- Oracle VirtualBox 7.x
- Ubuntu Server 24.04.3 LTS ISO
- Python 3.x

### Step 1: Install Dependencies (On Each VM)

```bash
sudo apt update
sudo apt install uvicorn
sudo apt install python3 python3-pip -y
pip3 install fastapi uvicorn requests
```

### Step 2: Deploy Services

**On VM1 (10.0.2.3):**
```bash
# Copy gateway.py to VM1
uvicorn gateway:app --host 0.0.0.0 --port 8001
```

**On VM2 (10.0.2.4):**
```bash
# Copy validator.py to VM2
uvicorn validator:app --host 0.0.0.0 --port 8002
```

**On VM3 (10.0.2.5):**
```bash
# Copy greeter.py to VM3
uvicorn greeter:app --host 0.0.0.0 --port 8003
```

## 🧪 Testing

### Success Test (Valid Input)

```bash
curl -X POST http://10.0.2.3:8001/ping \
  -H "Content-Type: application/json" \
  -d '{"name": "Anshul"}'
```

**Expected Output:**
```
==============================
           OUTPUT
==============================

Name: Anshul
Date: 2026-02-01
Time: 10:30:45

------------------------------

Path : VM1 to VM2 to VM3

------------------------------

Message: Hello Anshul, Welcome to VCC!

------------------------------

Status : Success!!!
==============================
```

### Failure Test (Empty Name)

```bash
curl -X POST http://10.0.2.3:8001/ping \
  -H "Content-Type: application/json" \
  -d '{"name": ""}'
```

**Expected Output:**
```
==========ERROR==========
 Validation Failed !
 Reason: Name cannot be empty
=========================
```

## 📁 Project Structure

```
.
├── vm1/
│   └── gateway.py      # API Gateway Service
├── vm2/
│   └── validator.py    # Validator Service
├── vm3/
│   └── greeter.py      # Greeter Service
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🔧 Network Configuration

### NAT Network Setup in VirtualBox

1. Go to **File → Tools → Network Manager → NAT Networks**
2. Click **Create** and configure:
   - Name: `MicroserviceNetwork`
   - IPv4 Prefix: `10.0.2.0/24`
   - Enable DHCP: ✅

3. For each VM, go to **Settings → Network**:
   - Attached to: `NAT Network`
   - Name: `MicroserviceNetwork`

## 📺 Demo Video

[Link to Video Demonstration](https://drive.google.com/file/d/1u4RM-ocTUhr9RO69Bd8Jx_2D6R8z8aOd/view?usp=sharing)

## 👤 Author

**Anshul Kumar**  
Indian Institute of Technology, Jodhpur

## 📄 License

This project is for educational purposes as part of the VCC course assignment.
