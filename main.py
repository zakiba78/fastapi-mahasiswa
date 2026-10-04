from fastapi import FastAPI

app = FastAPI(title="API Data Mahasiswa")


mahasiswa = [
    {
        "id": 1,
        "nama": "Muhammad Zaki",
        "alamat": "Bekasi",
        "ipk": 3.87,
        "semester": 5,
        "hobi": "Gaming"
    }
]


@app.get("/mahasiswa")
def get_mahasiswa():
    return mahasiswa
@app.post("/mahasiswa")
def tambah_mahasiswa(data: dict):
    data["id"] = len(mahasiswa) + 1
    mahasiswa.append(data)
    return data


@app.put("/mahasiswa/{id}")
def update_mahasiswa(id: int, data: dict):
    for mhs in mahasiswa:
        if mhs["id"] == id:
            mhs.update(data)
            mhs["id"] = id
            return mhs

    return {"message": "Mahasiswa tidak ditemukan"}


@app.delete("/mahasiswa/{id}")
def delete_mahasiswa(id: int):
    for mhs in mahasiswa:
        if mhs["id"] == id:
            mahasiswa.remove(mhs)
            return {"message": "Data berhasil dihapus"}

    return {"message": "Mahasiswa tidak ditemukan"}