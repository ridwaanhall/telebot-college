from urllib.parse import quote

import requests


class ReadUrl:

  def read_json(self, url):
    response = requests.get(url)
    if response.status_code == 200:
      return response.json()
    return None


# ============ STUDENTS ============================
class STUDENTS:
  

  def GetMhsList(self, message):
    reader = ReadUrl()
    url = 'https://api-frontend.kemdikbud.go.id/hit_mhs/'
    if message:
      encoded_message = quote(message)
      url += encoded_message
    getmhs_list = reader.read_json(url)
    if getmhs_list is None:
      return []

    if "Cari kata kunci" in getmhs_list.get("mahasiswa", [])[0]["text"]:
      return [{"text": getmhs_list["mahasiswa"][0]["text"]}]

    filtered_students = []
    for student in getmhs_list.get("mahasiswa", []):
      info = student["text"].split(", ")
      name = info[0].split("(")[0]
      id_number = info[0].split("(")[1].split(")")[0]
      college = info[1].split(" : ")[1]
      program = info[2].split(": ")[1]
      link = student["website-link"]
      link = link.replace("/data_mahasiswa", "")
      filtered_students.append({
        "name": name,
        "id_number": id_number,
        "college": college,
        "program": program,
        "website-link": link
      })

    return filtered_students