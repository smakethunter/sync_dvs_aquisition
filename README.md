# sync_dvs_aquisition
## Wymagane oprogramowanie

1. Akwizycja i konwersja do plików ```.dat```
- MetavisionSDK https://docs.prophesee.ai/stable/installation/index.html
lub  OpenEB:
https://github.com/prophesee-ai/openeb
2. Konwersja i Kalibracja
- Repozytorium e2vid:
https://github.com/uzh-rpg/e2calib/tree/main

Zalecana instalacja zgodnie z dokumentacją (conda env. Ważne dodanie metavision sdk do sys.path)
```
conda  develop <path>
```

## Kalibracja kamery zdarzeniowej

1. Akwizycja z systemu kamera zdarzeniowa i kamera wizyjna
- Kamera zdarzeniowa – startowy timestamp w nazwie pliku
- Kamera wizyjna  - Ramka oznaczona czasem pobrania (w nazwie lub logger)
2. Konwersja piku ```.raw```  ze zdarzeniami do formatu ```.h5``` akceptowanego przez e2vid
- ```.raw``` do ```.dat``` z metavision_sdk api:
```
metavision_file_to_dat -i FILE_NAME.raw
```
- z .dat do ```.h5``` przy wykorzystaniu sktryptu ```convert.py``` z pakietu e2calib
```
python3 convert.py FILENAME.dat --output_file OUT_FILENAME.h5
```
3. Przygotowanie timestampów ramek do konwersji e2vid – skrypt:  ```timestamps_e2vid.py```

4. Uzyskanie ramek z pliku ```.h5``` odnoszących się do timestampów wyznaczonych przez global shutter
```bash
python offline_reconstruction.py --timestamps_file <timestamps>.txt --upsample_rate 1 --h5file <file_in>.h5  --output_folder <folder_out> --height <height> --width  <width> 
```
5. Kalibracja z użyciem skryptu ```python_stereo_camera_calibration/calib.py``` – Wymaga modyfikacji ścieżek i pliku ```.yaml``` wg potrzeb.
```
python3 calib.py
```
