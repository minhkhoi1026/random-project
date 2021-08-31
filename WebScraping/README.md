# HCMUS GPA Calculator

This is an simple Python project using `beautiful soup` for crawling web data and calculate *(cummulative GPA, cummulative credit, expected credit)* for HCMUS student.

Explain:
- Cummulative GPA: overall GPA of all subject you learned (except Anh văn, Giáo dục Quốc phòng, Sinh hoạt công dân, Thể dục).
- Cummulative credit: total credit you learned
- Expected credit: Cummulative credit + this semester credit

## How to use
Follow these step:
1. Login to your HCMUS portal account
2. Navigate to *Quản lý học phần > Tra cứu kết quả học tập*
3. In *Năm học* field choose *Tất cả* and press *Xem kết quả học tập* button
4. Press `ctrl + S` to save web source (you should save it in this project directory)
5. Edit *PATH* variable in `.env` file, assign a path to HTML file you saved in the previous step.
6. Open your command line, move to this project directory and type following command:
- To install dependencies: `python install -r requirements.txt`
- To calculate GPA: `python GPAportal.py`