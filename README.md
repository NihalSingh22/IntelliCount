# IntelliCount - Advanced Vehicle Detection & Counting System

IntelliCount is a sophisticated OpenCV-based system designed to analyze video feeds of traffic and provide real-time, accurate vehicle counting. Utilizing advanced computer vision techniques, IntelliCount can effectively aid in traffic management, urban planning, and flow analysis.

## Background Process

<img width="1278" alt="Screen Shot 2024-03-04 at 8 16 10 PM" src="https://github.com/NihalSingh22/IntelliCount/assets/89406047/91163daf-ecd3-4a18-a81c-80e54fb87877">

The above image illustrates the initial stage of the vehicle detection process where the background is eliminated, isolating moving vehicles. This is a crucial step in ensuring the subsequent steps of vehicle detection and counting are accurate and efficient.

## Final Output


<img width="1268" alt="Screen Shot 2024-03-05 at 7 16 58 PM" src="https://github.com/NihalSingh22/IntelliCount/assets/89406047/47ae8768-98c8-4747-8576-6e9e7f0fdaba">
<img width="1253" alt="Screen Shot 2024-03-05 at 7 17 31 PM" src="https://github.com/NihalSingh22/IntelliCount/assets/89406047/6f162888-57f3-4afc-b0de-b5d3a06ce76f">


As seen in the final output images above, IntelliCount overlays the detected vehicles with bounding boxes, assigns a unique identifier to each, and displays a real-time count. This output showcases the system's accuracy in various traffic conditions.

## Features

- Real-time vehicle detection and counting from video feeds.
- Robust background subtraction for vehicle isolation.
- Adaptive bounding techniques to accommodate different vehicle sizes and shapes.
- Real-time counter updates as vehicles pass through the detection zone.

## Installation

To get IntelliCount up and running on your local machine, follow these steps:

```bash
git clone https://github.com/YOUR_GITHUB/IntelliCount.git
cd IntelliCount
# Ensure you have the required dependencies
pip install -r requirements.txt
# Run the system
python vehicle_counter.py
```

## Usage
To use IntelliCount with your own video feed, you can modify the video.mp4 path in the vehicle_counter.py script to the path of your video file.

- video_capture = cv2.VideoCapture('path_to_your_video.mp4')

Then simply run the script again as mentioned above.

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!


## Contact
Nihal Singh - nihalsinghdxb@gmail.com

Project Link: https://github.com/NihalSingh22/IntelliCount




















