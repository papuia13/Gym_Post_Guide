import { FilesetResolver, PoseLandmarker } from '@mediapipe/tasks-vision';

const startButton: HTMLElement | null = document.getElementById("startButton");
const video: HTMLVideoElement | null = document.getElementById("video") as HTMLVideoElement;

let poseLandmarker: PoseLandmarker | null = null;

async function initializePoseLandmarker(): Promise<void> {
  const vision = await FilesetResolver.forVisionTasks(
    "T:/MCA/3rd_Sem/ECP/Gym_Action_Tracker/node_modules/@mediapipe/tasks-vision/wasm"
  );

  poseLandmarker = await PoseLandmarker.createFromOptions(
    vision,
    {
      baseOptions: {
        modelAssetPath: "T:/MCA/3rd_Sem/ECP/Gym_Action_Tracker/Demo2/app/shared/models/pose_landmarker_lite.task",
      },
      runningMode: "VIDEO",
    }
  );
}

async function setupWebcam(): Promise<void> {
  if (!video) return;

  const stream = await navigator.mediaDevices.getUserMedia({ video: true });
  video.srcObject = stream;

  return new Promise<void>((resolve) => {
    video.onloadedmetadata = () => {
      video.play();
      resolve();
    };
  });
}

function processResults(poseLandmarkerResult: any): void {
  // Handle results here (e.g., log or visualize keypoints)
  console.log(poseLandmarkerResult);
}

async function renderLoop(): Promise<void> {
  if (!poseLandmarker || !video) return; // Ensure poseLandmarker and video are initialized

  let lastVideoTime = -1;

  if (video.currentTime !== lastVideoTime) {
    // Await the poseLandmarkerResult because detectForVideo is asynchronous
    const poseLandmarkerResult = await poseLandmarker.detectForVideo(video, video.currentTime);
    processResults(poseLandmarkerResult);
    lastVideoTime = video.currentTime;
  }

  // Continue rendering
  requestAnimationFrame(renderLoop);
}

async function startPoseEstimation(): Promise<void> {
  // Hide the button and show the video (camera feed)
  if (startButton) startButton.style.display = "none";
  if (video) video.style.display = "block";

  // Initialize pose landmarker and start webcam
  await initializePoseLandmarker();
  await setupWebcam();
  if (poseLandmarker) {
    await poseLandmarker.setOptions({ runningMode: "VIDEO" });
    renderLoop();
  }
}

// Add event listener to start button
if (startButton) {
  startButton.addEventListener("click", startPoseEstimation);
}