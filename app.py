#Danh sách để lưu các công việc 
task = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách"""
    task.append(task_name)
    print(f"Đã thêm công việc: {task_name}")
#---Điểm bắt đầu chương trình---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git and Github")
    add_task("Làm bài tập thực hành ở nhà")
