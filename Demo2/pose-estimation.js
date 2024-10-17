"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype);
    return g.next = verb(0), g["throw"] = verb(1), g["return"] = verb(2), typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
Object.defineProperty(exports, "__esModule", { value: true });
var tasks_vision_1 = require("@mediapipe/tasks-vision");
var startButton = document.getElementById("startButton");
var video = document.getElementById("video");
var poseLandmarker = null;
function initializePoseLandmarker() {
    return __awaiter(this, void 0, void 0, function () {
        var vision;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0: return [4 /*yield*/, tasks_vision_1.FilesetResolver.forVisionTasks("T:/MCA/3rd_Sem/ECP/Gym_Action_Tracker/node_modules/@mediapipe/tasks-vision/wasm")];
                case 1:
                    vision = _a.sent();
                    return [4 /*yield*/, tasks_vision_1.PoseLandmarker.createFromOptions(vision, {
                            baseOptions: {
                                modelAssetPath: "T:/MCA/3rd_Sem/ECP/Gym_Action_Tracker/Demo2/app/shared/models/pose_landmarker_lite.task",
                            },
                            runningMode: "VIDEO",
                        })];
                case 2:
                    poseLandmarker = _a.sent();
                    return [2 /*return*/];
            }
        });
    });
}
function setupWebcam() {
    return __awaiter(this, void 0, void 0, function () {
        var stream;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    if (!video)
                        return [2 /*return*/];
                    return [4 /*yield*/, navigator.mediaDevices.getUserMedia({ video: true })];
                case 1:
                    stream = _a.sent();
                    video.srcObject = stream;
                    return [2 /*return*/, new Promise(function (resolve) {
                            video.onloadedmetadata = function () {
                                video.play();
                                resolve();
                            };
                        })];
            }
        });
    });
}
function processResults(poseLandmarkerResult) {
    // Handle results here (e.g., log or visualize keypoints)
    console.log(poseLandmarkerResult);
}
function renderLoop() {
    return __awaiter(this, void 0, void 0, function () {
        var lastVideoTime, poseLandmarkerResult;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    if (!poseLandmarker || !video)
                        return [2 /*return*/]; // Ensure poseLandmarker and video are initialized
                    lastVideoTime = -1;
                    if (!(video.currentTime !== lastVideoTime)) return [3 /*break*/, 2];
                    return [4 /*yield*/, poseLandmarker.detectForVideo(video, video.currentTime)];
                case 1:
                    poseLandmarkerResult = _a.sent();
                    processResults(poseLandmarkerResult);
                    lastVideoTime = video.currentTime;
                    _a.label = 2;
                case 2:
                    // Continue rendering
                    requestAnimationFrame(renderLoop);
                    return [2 /*return*/];
            }
        });
    });
}
function startPoseEstimation() {
    return __awaiter(this, void 0, void 0, function () {
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    // Hide the button and show the video (camera feed)
                    if (startButton)
                        startButton.style.display = "none";
                    if (video)
                        video.style.display = "block";
                    // Initialize pose landmarker and start webcam
                    return [4 /*yield*/, initializePoseLandmarker()];
                case 1:
                    // Initialize pose landmarker and start webcam
                    _a.sent();
                    return [4 /*yield*/, setupWebcam()];
                case 2:
                    _a.sent();
                    if (!poseLandmarker) return [3 /*break*/, 4];
                    return [4 /*yield*/, poseLandmarker.setOptions({ runningMode: "VIDEO" })];
                case 3:
                    _a.sent();
                    renderLoop();
                    _a.label = 4;
                case 4: return [2 /*return*/];
            }
        });
    });
}
// Add event listener to start button
if (startButton) {
    startButton.addEventListener("click", startPoseEstimation);
}
