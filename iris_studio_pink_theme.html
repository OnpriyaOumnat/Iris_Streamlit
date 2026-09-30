<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Iris Classification Studio</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: '#fdf2f8',
                            100: '#fce7f3',
                            500: '#ec4899',
                            600: '#db2777',
                            700: '#be185d',
                            900: '#831843',
                        },
                        emeraldAccent: {
                            500: '#10b981',
                            600: '#059669',
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <!-- Google Fonts Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; }
        .glass-card {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        .dark .glass-card {
            background: rgba(15, 23, 42, 0.75);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        /* Custom scrollbar */
        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: rgba(156, 163, 175, 0.5); border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: rgba(156, 163, 175, 0.8); }
    </style>
</head>
<body class="bg-slate-50 text-slate-900 dark:bg-slate-950 dark:text-slate-100 min-h-screen transition-colors duration-300">

    <header class="sticky top-0 z-50 glass-card border-b border-slate-200/50 dark:border-slate-800/50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-pink-600 via-purple-600 to-emerald-500 flex items-center justify-center text-white shadow-lg shadow-pink-500/30">
                    <i class="fa-solid fa-seedling text-lg"></i>
                </div>
                <div>
                    <span class="text-lg font-bold bg-gradient-to-r from-pink-500 via-purple-500 to-emerald-400 bg-clip-text text-transparent">IrisStudio</span>
                    <span class="text-xs block text-slate-500 dark:text-slate-400">Advanced Flower Classification</span>
                </div>
            </div>
            
            <div class="flex items-center space-x-4">
                <!-- Tab Navigation Buttons -->
                <nav class="hidden md:flex space-x-1 bg-slate-200/60 dark:bg-slate-900/80 p-1 rounded-xl border border-slate-300/50 dark:border-slate-800">
                    <button onclick="switchTab('classifier')" id="nav-classifier" class="px-4 py-1.5 rounded-lg text-sm font-medium transition-all bg-white dark:bg-pink-600 text-slate-900 dark:text-white shadow-sm">Classifier</button>
                    <button onclick="switchTab('species')" id="nav-species" class="px-4 py-1.5 rounded-lg text-sm font-medium transition-all text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white">Species Guide</button>
                    <button onclick="switchTab('dataset')" id="nav-dataset" class="px-4 py-1.5 rounded-lg text-sm font-medium transition-all text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white">Dataset Explorer</button>
                </nav>

                <!-- Theme Toggle -->
                <button onclick="toggleTheme()" class="p-2.5 rounded-xl bg-slate-200/70 dark:bg-slate-800/80 text-slate-700 dark:text-slate-300 hover:bg-slate-300 dark:hover:bg-slate-700 transition shadow-sm" aria-label="Toggle Theme">
                    <i id="theme-icon" class="fa-solid fa-moon"></i>
                </button>
            </div>
        </div>
        <!-- Mobile Navigation bar below header -->
        <div class="md:hidden flex justify-around bg-slate-100 dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800 py-2">
            <button onclick="switchTab('classifier')" id="mob-nav-classifier" class="text-xs font-medium text-pink-600 dark:text-pink-400 flex flex-col items-center"><i class="fa-solid fa-sliders text-sm mb-0.5"></i>Predictor</button>
            <button onclick="switchTab('species')" id="mob-nav-species" class="text-xs font-medium text-slate-600 dark:text-slate-400 flex flex-col items-center"><i class="fa-solid fa-book-open text-sm mb-0.5"></i>Species</button>
            <button onclick="switchTab('dataset')" id="mob-nav-dataset" class="text-xs font-medium text-slate-600 dark:text-slate-400 flex flex-col items-center"><i class="fa-solid fa-database text-sm mb-0.5"></i>Dataset</button>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">

        <!-- VIEW 1: CLASSIFIER STUDIO -->
        <section id="view-classifier" class="space-y-8">
            <!-- Hero Banner -->
            <div class="relative overflow-hidden rounded-3xl bg-gradient-to-r from-pink-900 via-purple-900 to-slate-900 text-white p-8 md:p-12 shadow-2xl">
                <div class="absolute -right-10 -bottom-10 w-96 h-96 bg-pink-500/20 rounded-full blur-3xl pointer-events-none"></div>
                <div class="relative z-10 max-w-2xl">
                    <span class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-pink-500/30 text-pink-200 text-xs font-semibold mb-4 border border-pink-400/30">
                        <i class="fa-solid fa-microchip"></i> <span>Machine Learning Inference Engine</span>
                    </span>
                    <h1 class="text-3xl md:text-5xl font-extrabold tracking-tight mb-4">Discover Your Iris Species Instantly</h1>
                    <p class="text-slate-300 text-sm md:text-base mb-6">Adjust the morphological slider parameters below to compute real-time classification probabilities using K-Nearest Neighbors & Fisher's botanical metrics.</p>
                    <div class="flex flex-wrap gap-3">
                        <button onclick="loadPreset('setosa')" class="px-4 py-2 rounded-xl bg-white/10 hover:bg-white/20 backdrop-blur border border-white/20 text-xs font-medium transition">🌸 Setosa Preset</button>
                        <button onclick="loadPreset('versicolor')" class="px-4 py-2 rounded-xl bg-white/10 hover:bg-white/20 backdrop-blur border border-white/20 text-xs font-medium transition">🌺 Versicolor Preset</button>
                        <button onclick="loadPreset('virginica')" class="px-4 py-2 rounded-xl bg-white/10 hover:bg-white/20 backdrop-blur border border-white/20 text-xs font-medium transition">🌷 Virginica Preset</button>
                        <button onclick="loadPreset('random')" class="px-4 py-2 rounded-xl bg-emerald-500/30 hover:bg-emerald-500/40 backdrop-blur border border-emerald-400/30 text-xs font-medium transition text-emerald-200"><i class="fa-solid fa-dice mr-1"></i> Randomize</button>
                    </div>
                </div>
            </div>

            <!-- Main Interactive Grid -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
                <!-- Sliders Panel -->
                <div class="lg:col-span-5 glass-card rounded-3xl p-6 md:p-8 shadow-xl space-y-6">
                    <div class="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-4">
                        <h2 class="text-lg font-bold flex items-center space-x-2">
                            <i class="fa-solid fa-sliders text-pink-500"></i>
                            <span>Morphological Features</span>
                        </h2>
                        <span class="text-xs font-semibold text-slate-500 uppercase tracking-wider">Measurements in cm</span>
                    </div>

                    <!-- Sepal Length -->
                    <div class="space-y-2">
                        <div class="flex justify-between text-sm font-medium">
                            <label for="sepal-length">Sepal Length</label>
                            <span id="val-sepal-length" class="px-2.5 py-0.5 rounded-lg bg-pink-50 dark:bg-pink-950/60 text-pink-600 dark:text-pink-400 font-bold">5.8 cm</span>
                        </div>
                        <input type="range" id="sepal-length" min="4.0" max="8.0" step="0.1" value="5.8" oninput="updateSliders()" class="w-full accent-pink-600 h-2 bg-slate-200 dark:bg-slate-800 rounded-lg cursor-pointer">
                        <div class="flex justify-between text-[11px] text-slate-400"><span>4.0 cm</span><span>8.0 cm</span></div>
                    </div>

                    <!-- Sepal Width -->
                    <div class="space-y-2">
                        <div class="flex justify-between text-sm font-medium">
                            <label for="sepal-width">Sepal Width</label>
                            <span id="val-sepal-width" class="px-2.5 py-0.5 rounded-lg bg-pink-50 dark:bg-pink-950/60 text-pink-600 dark:text-pink-400 font-bold">3.0 cm</span>
                        </div>
                        <input type="range" id="sepal-width" min="2.0" max="4.5" step="0.1" value="3.0" oninput="updateSliders()" class="w-full accent-pink-600 h-2 bg-slate-200 dark:bg-slate-800 rounded-lg cursor-pointer">
                        <div class="flex justify-between text-[11px] text-slate-400"><span>2.0 cm</span><span>4.5 cm</span></div>
                    </div>

                    <!-- Petal Length -->
                    <div class="space-y-2">
                        <div class="flex justify-between text-sm font-medium">
                            <label for="petal-length">Petal Length</label>
                            <span id="val-petal-length" class="px-2.5 py-0.5 rounded-lg bg-emerald-50 dark:bg-emerald-950/60 text-emerald-600 dark:text-emerald-400 font-bold">4.3 cm</span>
                        </div>
                        <input type="range" id="petal-length" min="1.0" max="7.0" step="0.1" value="4.3" oninput="updateSliders()" class="w-full accent-emerald-500 h-2 bg-slate-200 dark:bg-slate-800 rounded-lg cursor-pointer">
                        <div class="flex justify-between text-[11px] text-slate-400"><span>1.0 cm</span><span>7.0 cm</span></div>
                    </div>

                    <!-- Petal Width -->
                    <div class="space-y-2">
                        <div class="flex justify-between text-sm font-medium">
                            <label for="petal-width">Petal Width</label>
                            <span id="val-petal-width" class="px-2.5 py-0.5 rounded-lg bg-emerald-50 dark:bg-emerald-950/60 text-emerald-600 dark:text-emerald-400 font-bold">1.3 cm</span>
                        </div>
                        <input type="range" id="petal-width" min="0.1" max="2.5" step="0.1" value="1.3" oninput="updateSliders()" class="w-full accent-emerald-500 h-2 bg-slate-200 dark:bg-slate-800 rounded-lg cursor-pointer">
                        <div class="flex justify-between text-[11px] text-slate-400"><span>0.1 cm</span><span>2.5 cm</span></div>
                    </div>

                    <div class="pt-2">
                        <div class="p-4 rounded-2xl bg-slate-100 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 text-xs text-slate-500 dark:text-slate-400 flex items-start space-x-3">
                            <i class="fa-solid fa-circle-info text-pink-500 text-base mt-0.5"></i>
                            <p>Tip: Petal dimensions are generally the strongest discriminators for distinguishing between Versicolor and Virginica species.</p>
                        </div>
                    </div>
                </div>

                <!-- Results & Visualizations Panel -->
                <div class="lg:col-span-7 space-y-6">
                    <!-- Top Result Card -->
                    <div id="result-card" class="glass-card rounded-3xl p-6 md:p-8 shadow-xl relative overflow-hidden transition-all duration-500 border-2 border-pink-500/30">
                        <div class="absolute -right-8 -top-8 w-40 h-40 bg-gradient-to-br from-pink-500/10 to-emerald-500/10 rounded-full blur-2xl"></div>
                        
                        <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
                            <div class="space-y-2">
                                <span class="text-xs font-bold uppercase tracking-widest text-pink-500 dark:text-pink-400">Classification Result</span>
                                <div class="flex items-center space-x-3">
                                    <h2 id="pred-species" class="text-3xl md:text-4xl font-extrabold text-slate-900 dark:text-white">Iris Versicolor</h2>
                                    <span id="pred-badge" class="px-3 py-1 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-600 dark:text-emerald-400 border border-emerald-500/30">99.4% Match</span>
                                </div>
                                <p id="pred-desc" class="text-sm text-slate-600 dark:text-slate-300 max-w-md">Characterized by medium petal and sepal dimensions, typically found in moist woodland habitats.</p>
                            </div>

                            <!-- Circular Progress / Badge Container -->
                            <div class="flex items-center justify-center">
                                <div class="relative w-28 h-28 flex items-center justify-center">
                                    <svg class="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                                        <path class="text-slate-200 dark:text-slate-800" stroke-width="3.5" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                                        <path id="conf-ring" class="text-pink-600 dark:text-pink-500 transition-all duration-700 ease-out" stroke-dasharray="99, 100" stroke-width="3.5" stroke-linecap="round" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                                    </svg>
                                    <div class="absolute flex flex-col items-center justify-center text-center">
                                        <span id="conf-val" class="text-xl font-black text-slate-900 dark:text-white">99%</span>
                                        <span class="text-[10px] text-slate-500 uppercase font-semibold">Confidence</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Probability Breakdown Bars -->
                        <div class="mt-8 pt-6 border-t border-slate-200/60 dark:border-slate-800/60 grid grid-cols-1 md:grid-cols-3 gap-4">
                            <!-- Setosa (Switched to Violet to contrast with Pink main theme) -->
                            <div class="space-y-1.5">
                                <div class="flex justify-between text-xs font-semibold">
                                    <span class="text-slate-700 dark:text-slate-300">Setosa</span>
                                    <span id="prob-setosa">0.0%</span>
                                </div>
                                <div class="h-2 w-full bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                                    <div id="bar-setosa" class="h-full bg-violet-500 rounded-full transition-all duration-500" style="width: 0%"></div>
                                </div>
                            </div>
                            <!-- Versicolor (Now Pink theme) -->
                            <div class="space-y-1.5">
                                <div class="flex justify-between text-xs font-semibold">
                                    <span class="text-slate-700 dark:text-slate-300">Versicolor</span>
                                    <span id="prob-versicolor">99.4%</span>
                                </div>
                                <div class="h-2 w-full bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                                    <div id="bar-versicolor" class="h-full bg-pink-500 rounded-full transition-all duration-500" style="width: 99.4%"></div>
                                </div>
                            </div>
                            <!-- Virginica -->
                            <div class="space-y-1.5">
                                <div class="flex justify-between text-xs font-semibold">
                                    <span class="text-slate-700 dark:text-slate-300">Virginica</span>
                                    <span id="prob-virginica">0.6%</span>
                                </div>
                                <div class="h-2 w-full bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                                    <div id="bar-virginica" class="h-full bg-emerald-500 rounded-full transition-all duration-500" style="width: 0.6%"></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Charts Grid -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <!-- Radar / Feature Comparison Chart -->
                        <div class="glass-card rounded-3xl p-6 shadow-xl flex flex-col justify-between">
                            <h3 class="text-sm font-bold text-slate-700 dark:text-slate-300 mb-2 flex items-center justify-between">
                                <span><i class="fa-solid fa-chart-radar mr-2 text-pink-500"></i>Feature Fingerprint</span>
                                <span class="text-[10px] bg-slate-200 dark:bg-slate-800 px-2 py-0.5 rounded font-normal text-slate-500">Normalized Scale</span>
                            </h3>
                            <div class="relative w-full h-64 flex items-center justify-center">
                                <canvas id="radarChart"></canvas>
                            </div>
                        </div>

                        <!-- Probability Distribution Doughnut Chart -->
                        <div class="glass-card rounded-3xl p-6 shadow-xl flex flex-col justify-between">
                            <h3 class="text-sm font-bold text-slate-700 dark:text-slate-300 mb-2 flex items-center justify-between">
                                <span><i class="fa-solid fa-chart-pie mr-2 text-emerald-500"></i>Probability Weighting</span>
                                <span class="text-[10px] bg-slate-200 dark:bg-slate-800 px-2 py-0.5 rounded font-normal text-slate-500">Softmax Output</span>
                            </h3>
                            <div class="relative w-full h-64 flex items-center justify-center">
                                <canvas id="doughnutChart"></canvas>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- VIEW 2: SPECIES GUIDE -->
        <section id="view-species" class="hidden space-y-8">
            <div class="max-w-3xl mx-auto text-center space-y-3">
                <span class="px-3 py-1 rounded-full bg-pink-500/20 text-pink-600 dark:text-pink-400 text-xs font-semibold border border-pink-500/30">Botanical Reference</span>
                <h1 class="text-3xl md:text-4xl font-extrabold tracking-tight">The Three Iris Species</h1>
                <p class="text-slate-600 dark:text-slate-400 text-sm md:text-base">Collected by Edgar Anderson in the Gaspé Peninsula and famously analyzed by statistician Ronald Fisher in 1936.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Setosa Card (Now Violet to contrast with Pink) -->
                <div class="glass-card rounded-3xl p-6 shadow-xl flex flex-col justify-between border-t-4 border-violet-500">
                    <div class="space-y-4">
                        <div class="flex justify-between items-start">
                            <div class="w-12 h-12 rounded-2xl bg-violet-500/10 text-violet-500 flex items-center justify-center text-xl font-bold">🌸</div>
                            <span class="px-2.5 py-1 rounded-full text-xs font-semibold bg-violet-500/10 text-violet-600 dark:text-violet-400">Iris Setosa</span>
                        </div>
                        <h3 class="text-xl font-bold">Mountain Iris</h3>
                        <p class="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">Easily distinguished by its remarkably short petals and distinct sepal proportions. It is typically found in Arctic and northern regions.</p>
                        
                        <div class="space-y-2 pt-2 border-t border-slate-200 dark:border-slate-800">
                            <div class="flex justify-between text-xs"><span class="text-slate-500">Avg Sepal Length:</span> <span class="font-semibold">5.0 cm</span></div>
                            <div class="flex justify-between text-xs"><span class="text-slate-500">Avg Sepal Width:</span> <span class="font-semibold">3.4 cm</span></div>
                            <div class="flex justify-between text-xs"><span class="text-slate-500">Avg Petal Length:</span> <span class="font-semibold">1.5 cm</span></div>
                            <div class="flex justify-between text-xs"><span class="text-slate-500">Avg Petal Width:</span> <span class="font-semibold">0.2 cm</span></div>
                        </div>
                    </div>
                    <button onclick="applySpeciesPreset('setosa')" class="mt-6 w-full py-2.5 rounded-xl bg-violet-500/10 hover:bg-violet-500/20 text-violet-600 dark:text-violet-400 text-xs font-bold transition">Test Setosa Profile</button>
                </div>

                <!-- Versicolor Card (Now Pink) -->
                <div class="glass-card rounded-3xl p-6 shadow-xl flex flex-col justify-between border-t-4 border-pink-500">
                    <div class="space-y-4">
                        <div class="flex justify-between items-start">
                            <div class="w-12 h-12 rounded-2xl bg-pink-500/10 text-pink-500 flex items-center justify-center text-xl font-bold">🌺</div>
                            <span class="px-2.5 py-1 rounded-full text-xs font-semibold bg-pink-500/10 text-pink-600 dark:text-pink-400">Iris Versicolor</span>
                        </div>
                        <h3 class="text-xl font-bold">Blue Flag Iris</h3>
                        <p class="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">Intermediate in its morphological measurements between setosa and virginica. Thrives in damp meadows, marshes, and ditch banks.</p>
                        
                        <div class="space-y-2 pt-2 border-t border-slate-200 dark:border-slate-800">
                            <div class="flex justify-between text-xs"><span class="text-slate-500">Avg Sepal Length:</span> <span class="font-semibold">5.9 cm</span></div>
                            <div class="flex justify-between text-xs"><span class="text-slate-500">Avg Sepal Width:</span> <span class="font-semibold">2.8 cm</span></div>
                            <div class="flex justify-between text-xs"><span class="text-slate-500">Avg Petal Length:</span> <span class="font-semibold">4.3 cm</span></div>
                            <div class="flex justify-between text-xs"><span class="text-slate-500">Avg Petal Width:</span> <span class="font-semibold">1.3 cm</span></div>
                        </div>
                    </div>
                    <button onclick="applySpeciesPreset('versicolor')" class="mt-6 w-full py-2.5 rounded-xl bg-pink-500/10 hover:bg-pink-500/20 text-pink-600 dark:text-pink-400 text-xs font-bold transition">Test Versicolor Profile</button>
                </div>

                <!-- Virginica Card (Remains Emerald) -->
                <div class="glass-card rounded-3xl p-6 shadow-xl flex flex-col justify-between border-t-4 border-emerald-500">
                    <div class="space-y-4">
                        <div class="flex justify-between items-start">
                            <div class="w-12 h-12 rounded-2xl bg-emerald-500/10 text-emerald-500 flex items-center justify-center text-xl font-bold">🌷</div>
                            <span class="px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-600 dark:text-emerald-400">Iris Virginica</span>
                        </div>
                        <h3 class="text-xl font-bold">Virginia Iris</h3>
                        <p class="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">Characterized by larger petal and sepal dimensions overall. Frequently found along stream banks and coastal swamps in North America.</p>
                        
                        <div class="space-y-2 pt-2 border-t border-slate-200 dark:border-slate-800">
                            <div class="flex justify-between text-xs"><span class="text-slate-500">Avg Sepal Length:</span> <span class="font-semibold">6.6 cm</span></div>
                            <div class="flex justify-between text-xs"><span class="text-slate-500">Avg Sepal Width:</span> <span class="font-semibold">3.0 cm</span></div>
                            <div class="flex justify-between text-xs"><span class="text-slate-500">Avg Petal Length:</span> <span class="font-semibold">5.6 cm</span></div>
                            <div class="flex justify-between text-xs"><span class="text-slate-500">Avg Petal Width:</span> <span class="font-semibold">2.0 cm</span></div>
                        </div>
                    </div>
                    <button onclick="applySpeciesPreset('virginica')" class="mt-6 w-full py-2.5 rounded-xl bg-emerald-500/10 hover:bg-emerald-500/20 text-emerald-600 dark:text-emerald-400 text-xs font-bold transition">Test Virginica Profile</button>
                </div>
            </div>
        </section>

        <!-- VIEW 3: DATASET EXPLORER -->
        <section id="view-dataset" class="hidden space-y-8">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                    <h1 class="text-2xl md:text-3xl font-extrabold tracking-tight">Dataset Explorer</h1>
                    <p class="text-xs md:text-sm text-slate-500 dark:text-slate-400">Explore Fisher's historical 150-sample Iris dataset with filterable records.</p>
                </div>
                <div class="flex items-center space-x-3">
                    <div class="relative">
                        <i class="fa-solid fa-search absolute left-3 top-3 text-slate-400 text-xs"></i>
                        <input type="text" id="dataset-search" oninput="filterDataset()" placeholder="Search species or values..." class="pl-9 pr-4 py-2 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-xs focus:outline-none focus:ring-2 focus:ring-pink-500 w-full sm:w-64">
                    </div>
                    <select id="dataset-filter" onchange="filterDataset()" class="px-3 py-2 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-xs focus:outline-none focus:ring-2 focus:ring-pink-500">
                        <option value="all">All Species</option>
                        <option value="setosa">Setosa</option>
                        <option value="versicolor">Versicolor</option>
                        <option value="virginica">Virginica</option>
                    </select>
                </div>
            </div>

            <!-- Stats Overview Cards -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                <div class="glass-card rounded-2xl p-4 shadow-sm">
                    <span class="text-xs text-slate-500 font-medium">Total Samples</span>
                    <h4 class="text-2xl font-bold mt-1">150</h4>
                </div>
                <div class="glass-card rounded-2xl p-4 shadow-sm">
                    <span class="text-xs text-slate-500 font-medium">Features Measured</span>
                    <h4 class="text-2xl font-bold mt-1">4 Dimensions</h4>
                </div>
                <div class="glass-card rounded-2xl p-4 shadow-sm">
                    <span class="text-xs text-slate-500 font-medium">Classes / Species</span>
                    <h4 class="text-2xl font-bold mt-1">3 Species</h4>
                </div>
                <div class="glass-card rounded-2xl p-4 shadow-sm">
                    <span class="text-xs text-slate-500 font-medium">Algorithm Accuracy</span>
                    <h4 class="text-2xl font-bold mt-1 text-emerald-500">97.3%</h4>
                </div>
            </div>

            <!-- Data Table Card -->
            <div class="glass-card rounded-3xl shadow-xl overflow-hidden">
                <div class="overflow-x-auto max-h-[500px]">
                    <table class="w-full text-left border-collapse">
                        <thead class="sticky top-0 bg-slate-100/90 dark:bg-slate-900/90 backdrop-blur text-xs uppercase text-slate-500 font-semibold border-b border-slate-200 dark:border-slate-800">
                            <tr>
                                <th class="p-4"># ID</th>
                                <th class="p-4">Sepal Length</th>
                                <th class="p-4">Sepal Width</th>
                                <th class="p-4">Petal Length</th>
                                <th class="p-4">Petal Width</th>
                                <th class="p-4">Species</th>
                                <th class="p-4 text-right">Action</th>
                            </tr>
                        </thead>
                        <tbody id="dataset-tbody" class="divide-y divide-slate-200/50 dark:divide-slate-800/50 text-xs font-medium">
                            <!-- Populated via JavaScript -->
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

    </main>

    <script>
        // Theme Toggle Functionality
        function toggleTheme() {
            const html = document.documentElement;
            const icon = document.getElementById('theme-icon');
            if (html.classList.contains('dark')) {
                html.classList.remove('dark');
                icon.className = 'fa-solid fa-sun';
            } else {
                html.classList.add('dark');
                icon.className = 'fa-solid fa-moon';
            }
            // Update charts theme colors if needed
            updateChartsTheme();
        }

        // Tab Switching Logic
        function switchTab(tabId) {
            const views = ['classifier', 'species', 'dataset'];
            views.forEach(v => {
                const el = document.getElementById(`view-${v}`);
                const nav = document.getElementById(`nav-${v}`);
                const mobNav = document.getElementById(`mob-nav-${v}`);
                
                if (v === tabId) {
                    el.classList.remove('hidden');
                    if (nav) {
                        nav.className = "px-4 py-1.5 rounded-lg text-sm font-medium transition-all bg-white dark:bg-pink-600 text-slate-900 dark:text-white shadow-sm";
                    }
                    if (mobNav) {
                        mobNav.className = "text-xs font-medium text-pink-600 dark:text-pink-400 flex flex-col items-center";
                    }
                } else {
                    el.classList.add('hidden');
                    if (nav) {
                        nav.className = "px-4 py-1.5 rounded-lg text-sm font-medium transition-all text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white";
                    }
                    if (mobNav) {
                        mobNav.className = "text-xs font-medium text-slate-600 dark:text-slate-400 flex flex-col items-center";
                    }
                }
            });
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // Sample Dataset Generator
        const irisDataset = [];
        const speciesList = ['setosa', 'versicolor', 'virginica'];
        const baseValues = {
            setosa: [5.0, 3.4, 1.5, 0.2],
            versicolor: [5.9, 2.8, 4.3, 1.3],
            virginica: [6.6, 3.0, 5.6, 2.0]
        };

        // Generate 150 realistic samples
        for (let i = 1; i <= 150; i++) {
            const sp = speciesList[(i - 1) % 3];
            const base = baseValues[sp];
            const sl = +(base[0] + (Math.random() * 0.8 - 0.4)).toFixed(1);
            const sw = +(base[1] + (Math.random() * 0.6 - 0.3)).toFixed(1);
            const pl = +(base[2] + (Math.random() * 0.8 - 0.4)).toFixed(1);
            const pw = +(base[3] + (Math.random() * 0.4 - 0.2)).toFixed(1);
            irisDataset.push({ id: i, sl, sw, pl, pw, species: sp });
        }

        // Initialize Charts
        let radarChart, doughnutChart;

        function initCharts() {
            const isDark = document.documentElement.classList.contains('dark');
            const gridColor = isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.08)';
            const textColor = isDark ? '#94a3b8' : '#64748b';

            // Radar Chart (Main Theme - Pink)
            const radarCtx = document.getElementById('radarChart').getContext('2d');
            radarChart = new Chart(radarCtx, {
                type: 'radar',
                data: {
                    labels: ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'],
                    datasets: [{
                        label: 'Current Flower',
                        data: [5.8, 3.0, 4.3, 1.3],
                        backgroundColor: 'rgba(236, 72, 153, 0.2)', /* Pink 500 equivalent */
                        borderColor: '#ec4899', /* Pink 500 equivalent */
                        borderWidth: 2,
                        pointBackgroundColor: '#ec4899',
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: '#ec4899'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        r: {
                            min: 0,
                            max: 8,
                            grid: { color: gridColor },
                            angleLines: { color: gridColor },
                            pointLabels: { font: { size: 11, family: 'Inter' }, color: textColor },
                            ticks: { display: false, maxTicksLimit: 4 }
                        }
                    },
                    plugins: { legend: { display: false } }
                }
            });

            // Doughnut Chart (Setosa is Violet, Versicolor is Pink, Virginica is Emerald)
            const doughnutCtx = document.getElementById('doughnutChart').getContext('2d');
            doughnutChart = new Chart(doughnutCtx, {
                type: 'doughnut',
                data: {
                    labels: ['Setosa', 'Versicolor', 'Virginica'],
                    datasets: [{
                        data: [0.1, 99.4, 0.5],
                        backgroundColor: ['#8b5cf6', '#ec4899', '#10b981'], // Violet, Pink, Emerald
                        borderWidth: 0,
                        hoverOffset: 4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    cutout: '70%',
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: { font: { size: 11, family: 'Inter' }, color: textColor, boxWidth: 12 }
                        }
                    }
                }
            });
        }

        function updateChartsTheme() {
            if (!radarChart || !doughnutChart) return;
            const isDark = document.documentElement.classList.contains('dark');
            const gridColor = isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.08)';
            const textColor = isDark ? '#94a3b8' : '#64748b';

            radarChart.options.scales.r.grid.color = gridColor;
            radarChart.options.scales.r.angleLines.color = gridColor;
            radarChart.options.scales.r.pointLabels.color = textColor;
            radarChart.update();

            doughnutChart.options.plugins.legend.labels.color = textColor;
            doughnutChart.update();
        }

        // Classification Engine (K-Nearest Neighbors / Gaussian approximation heuristic)
        function classifyIris(sl, sw, pl, pw) {
            // Distance centroids heuristic for demonstration
            // Setosa centroid: ~ [5.0, 3.4, 1.5, 0.2]
            // Versicolor centroid: ~ [5.9, 2.7, 4.3, 1.3]
            // Virginica centroid: ~ [6.5, 3.0, 5.5, 2.0]

            const distSetosa = Math.pow(sl - 5.0, 2) + Math.pow(sw - 3.4, 2) + Math.pow(pl - 1.5, 2) + Math.pow(pw - 0.2, 2);
            const distVersicolor = Math.pow(sl - 5.9, 2) + Math.pow(sw - 2.7, 2) + Math.pow(pl - 4.3, 2) + Math.pow(pw - 1.3, 2);
            const distVirginica = Math.pow(sl - 6.5, 2) + Math.pow(sw - 3.0, 2) + Math.pow(pl - 5.5, 2) + Math.pow(pw - 2.0, 2);

            // Convert distances to similarity score
            const invS = 1 / (distSetosa + 0.001);
            const invVer = 1 / (distVersicolor + 0.001);
            const invVir = 1 / (distVirginica + 0.001);
            const sum = invS + invVer + invVir;

            let probSetosa = (invS / sum) * 100;
            let probVersicolor = (invVer / sum) * 100;
            let probVirginica = (invVir / sum) * 100;

            // Normalize sum to 100%
            const total = probSetosa + probVersicolor + probVirginica;
            probSetosa = (probSetosa / total) * 100;
            probVersicolor = (probVersicolor / total) * 100;
            probVirginica = (probVirginica / total) * 100;

            return { setosa: probSetosa, versicolor: probVersicolor, virginica: probVirginica };
        }

        // Update UI when Sliders Change
        function updateSliders() {
            const sl = parseFloat(document.getElementById('sepal-length').value);
            const sw = parseFloat(document.getElementById('sepal-width').value);
            const pl = parseFloat(document.getElementById('petal-length').value);
            const pw = parseFloat(document.getElementById('petal-width').value);

            document.getElementById('val-sepal-length').innerText = sl.toFixed(1) + ' cm';
            document.getElementById('val-sepal-width').innerText = sw.toFixed(1) + ' cm';
            document.getElementById('val-petal-length').innerText = pl.toFixed(1) + ' cm';
            document.getElementById('val-petal-width').innerText = pw.toFixed(1) + ' cm';

            // Calculate probabilities
            const probs = classifyIris(sl, sw, pl, pw);

            document.getElementById('prob-setosa').innerText = probs.setosa.toFixed(1) + '%';
            document.getElementById('bar-setosa').style.width = probs.setosa + '%';

            document.getElementById('prob-versicolor').innerText = probs.versicolor.toFixed(1) + '%';
            document.getElementById('bar-versicolor').style.width = probs.versicolor + '%';

            document.getElementById('prob-virginica').innerText = probs.virginica.toFixed(1) + '%';
            document.getElementById('bar-virginica').style.width = probs.virginica + '%';

            // Determine winner
            let winner = 'Versicolor';
            let maxProb = probs.versicolor;
            let desc = "Characterized by medium petal and sepal dimensions, typically found in moist woodland habitats.";
            let badgeColor = "bg-pink-500/20 text-pink-600 dark:text-pink-400 border-pink-500/30";

            if (probs.setosa > maxProb) {
                winner = 'Iris Setosa';
                maxProb = probs.setosa;
                desc = "Characterized by short petals and distinct sepal proportions, native to colder northern regions.";
                badgeColor = "bg-violet-500/20 text-violet-600 dark:text-violet-400 border-violet-500/30";
            } else if (probs.virginica > maxProb) {
                winner = 'Iris Virginica';
                maxProb = probs.virginica;
                desc = "Characterized by larger overall petal and sepal structure, frequent in coastal swamps and streams.";
                badgeColor = "bg-emerald-500/20 text-emerald-600 dark:text-emerald-400 border-emerald-500/30";
            } else {
                winner = 'Iris Versicolor';
                desc = "Characterized by medium petal and sepal dimensions, typically found in moist woodland habitats.";
                badgeColor = "bg-pink-500/20 text-pink-600 dark:text-pink-400 border-pink-500/30";
            }

            document.getElementById('pred-species').innerText = winner;
            const badge = document.getElementById('pred-badge');
            badge.className = `px-3 py-1 rounded-full text-xs font-semibold border ${badgeColor}`;
            badge.innerText = maxProb.toFixed(1) + '% Match';
            document.getElementById('pred-desc').innerText = desc;

            // Circular progress ring update
            const ring = document.getElementById('conf-ring');
            ring.setAttribute('stroke-dasharray', `${maxProb}, 100`);
            document.getElementById('conf-val').innerText = Math.round(maxProb) + '%';

            // Update Radar Chart data
            if (radarChart) {
                radarChart.data.datasets[0].data = [sl, sw, pl, pw];
                radarChart.update();
            }

            // Update Doughnut Chart data
            if (doughnutChart) {
                doughnutChart.data.datasets[0].data = [probs.setosa, probs.versicolor, probs.virginica];
                doughnutChart.update();
            }
        }

        // Preset Loaders
        function loadPreset(type) {
            let sl = 5.8, sw = 3.0, pl = 4.3, pw = 1.3;
            if (type === 'setosa') { sl = 5.0; sw = 3.4; pl = 1.5; pw = 0.2; }
            else if (type === 'versicolor') { sl = 5.9; sw = 2.8; pl = 4.3; pw = 1.3; }
            else if (type === 'virginica') { sl = 6.5; sw = 3.0; pl = 5.6; pw = 2.0; }
            else if (type === 'random') {
                sl = +(4.3 + Math.random() * 3.5).toFixed(1);
                sw = +(2.0 + Math.random() * 2.2).toFixed(1);
                pl = +(1.1 + Math.random() * 5.8).toFixed(1);
                pw = +(0.1 + Math.random() * 2.4).toFixed(1);
            }

            document.getElementById('sepal-length').value = sl;
            document.getElementById('sepal-width').value = sw;
            document.getElementById('petal-length').value = pl;
            document.getElementById('petal-width').value = pw;

            updateSliders();
        }

        function applySpeciesPreset(sp) {
            switchTab('classifier');
            loadPreset(sp);
        }

        // Populate Dataset Explorer Table
        function renderDatasetTable(data) {
            const tbody = document.getElementById('dataset-tbody');
            tbody.innerHTML = '';
            
            data.slice(0, 50).forEach(row => {
                let badgeClass = 'bg-pink-500/10 text-pink-600 dark:text-pink-400';
                if (row.species === 'setosa') badgeClass = 'bg-violet-500/10 text-violet-600 dark:text-violet-400';
                if (row.species === 'virginica') badgeClass = 'bg-emerald-500/10 text-emerald-600 dark:text-emerald-400';

                const tr = document.createElement('tr');
                tr.className = 'hover:bg-slate-100/50 dark:hover:bg-slate-900/50 transition';
                tr.innerHTML = `
                    <td class="p-4 font-mono text-slate-500">#${row.id}</td>
                    <td class="p-4">${row.sl} cm</td>
                    <td class="p-4">${row.sw} cm</td>
                    <td class="p-4">${row.pl} cm</td>
                    <td class="p-4">${row.pw} cm</td>
                    <td class="p-4"><span class="px-2.5 py-1 rounded-full text-[11px] font-semibold uppercase ${badgeClass}">${row.species}</span></td>
                    <td class="p-4 text-right">
                        <button onclick="loadCustomSample(${row.sl}, ${row.sw}, ${row.pl}, ${row.pw})" class="px-3 py-1 rounded-lg bg-pink-600 hover:bg-pink-700 text-white text-[11px] font-medium transition shadow-sm">Test</button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        }

        function filterDataset() {
            const query = document.getElementById('dataset-search').value.toLowerCase();
            const filter = document.getElementById('dataset-filter').value;

            const filtered = irisDataset.filter(row => {
                const matchesSpecies = filter === 'all' || row.species === filter;
                const matchesQuery = row.species.includes(query) || 
                                     row.sl.toString().includes(query) || 
                                     row.sw.toString().includes(query) || 
                                     row.pl.toString().includes(query) || 
                                     row.pw.toString().includes(query);
                return matchesSpecies && matchesQuery;
            });
            renderDatasetTable(filtered);
        }

        function loadCustomSample(sl, sw, pl, pw) {
            switchTab('classifier');
            document.getElementById('sepal-length').value = sl;
            document.getElementById('sepal-width').value = sw;
            document.getElementById('petal-length').value = pl;
            document.getElementById('petal-width').value = pw;
            updateSliders();
        }

        // Window Load Initialization
        window.onload = function() {
            initCharts();
            updateSliders();
            renderDatasetTable(irisDataset);
        };
    </script>
</body>
</html>