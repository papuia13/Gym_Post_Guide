const vision = await FilesetResolver.forVisionTasks(
    "T:/MCA/3rd_Sem/ECP/Gym_Action_Tracker/node_modules/@mediapipe/tasks-vision/wasm"
  );
  const poseLandmarker = await poseLandmarker.createFromOptions(
      vision,
      {
        baseOptions: {
          modelAssetPath: "T:/MCA/3rd_Sem/ECP/Gym_Action_Tracker/Demo2/app/shared/models/pose_landmarker_lite.task"
        },
        runningMode: "VIDEO"
      });

      await poseLandmarker.setOptions({ runningMode: "VIDEO" });

      let lastVideoTime = -1;
      function renderLoop(): void {
        const video = document.getElementById("video");
      
        if (video.currentTime !== lastVideoTime) {
          const poseLandmarkerResult = poseLandmarker.detectForVideo(video);
          processResults(detections);
          lastVideoTime = video.currentTime;
        }
      
        requestAnimationFrame(() => {
          renderLoop();
        });
      }