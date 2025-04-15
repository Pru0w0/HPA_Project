# HPA_Project
For AMD user
```plaintext
docker pull natyaninchayanuwong/hpa-project-amd
```
For ARM user : 
```plaintext
docker pull natyaninchayanuwong/hpa-project
```

# Project structure
```plaintext
HPA_Project
├── data
│   ├── input
│   └── output
├── docker-compose.yml
├── Dockerfile
├── HPA_Project_ortools.py
├── README.md
└── requirements.txt
```

# Usage
AMD user Command
```plaintext
time docker run -v ./data/input:/input  -v ./data/output:/output natyaninchayanuwong/hpa-project-amd /input/grid-6-7.txt /output/grid-6-7.out
```

Note : you need folder data which has input folder and out folder where you run command above


ARM user Command
```plaintext
time docker-compose up 
```
