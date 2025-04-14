# 🌍 GeoNetwork Converter

A simple Python 🐍 tool that transforms a shapefile of terrain vertices into a lightweight graph of **nodes** and **arcs**, with spatial and elevation data. Perfect for GIS nerds working on pathfinding, elevation-aware routing, or geonetwork simplification.

---

## ✨ Features

✅ Reads shapefiles with point geometries and elevation  
✅ Creates unique `SimpleNode` objects with coordinates and height  
✅ Links nodes into `SimpleArc` objects based on shared arc IDs  
✅ Outputs clean, structured JSON 📦 files for further processing or visualization

---

## 📁 Project Structure

```
📂 your_project/
├── main.py               # Main script
├── classes.py            # Node & Arc class definitions
├── vertices_height_split.shp  # Input shapefile (you provide this)
├── node_json.json        # Output: node network
├── arc_json.json         # Output: arc connections
```

---

## 📄 Output Format

### 🧩 Node example
```json
{
  "id": 0,
  "coordinates": {
    "x": 123456.78,
    "y": 987654.32
  },
  "height": 45.67,
  "arcs": [1, 2]
}
```

### 🔗 Arc example
```json
{
  "id": 1,
  "coordinates": {
    "start": {
      "node_id": 0,
      "x": 123456.78,
      "y": 987654.32,
      "height": 45.67
    },
    "end": {
      "node_id": 1,
      "x": 123400.00,
      "y": 987600.00,
      "height": 40.00
    }
  },
  "distance": 25.32,
  "elev_diff": 5.67,
  "direction": true
}
```

---

## 📦 Requirements

- Python 3.7+
- `geopandas`
- `shapely`

### 🔧 Setup
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install geopandas shapely
```

---

## 🚀 How to Run

1. Make sure `vertices_height_split.shp` (your input file) is in the same folder.
2. Run the script:
```bash
python shape_reader.py
```
3. Get your results in:
   - `node_json.json` 🟢
   - `arc_json.json` 🔵

---

## 📌 Notes

- Shapefile must include:
  - Point geometry (e.g., from a vertex split)
  - `ORIG_FID` field (to group arcs)
  - `RASTERVALU` or similar for elevation

---

## 📜 License

📝 MIT License – see [LICENSE](LICENSE)

---

## 🙌 Contributions

Pull requests, issues, and suggestions are welcome!  
If this helped you, give it a ⭐️ on GitHub!
