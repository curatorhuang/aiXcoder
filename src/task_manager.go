package main

import (
	"fmt"
	"time"
)

// Task 代表一个任务
type Task struct {
	ID        int
	Name      string
	Completed bool
	CreatedAt time.Time
}

// TaskManager 管理任务的结构体
type TaskManager struct {
	tasks   []Task
	nextID  int
}

// AddTask 添加一个新的任务
func (tm *TaskManager) AddTask(name string) {
	task := Task{
		ID:        tm.nextID,
		Name:      name,
		Completed: false,
		CreatedAt: time.Now(),
	}
	tm.tasks = append(tm.tasks, task)
	tm.nextID++
}

// CompleteTask 标记任务为完成
func (tm *TaskManager) CompleteTask(id int) {
	for i, task := range tm.tasks {
		if task.ID == id {
			tm.tasks[i].Completed = true
			return
		}
	}
}

// DeleteTask 删除任务
func (tm *TaskManager) DeleteTask(id int) {
	for i, task := range tm.tasks {
		if task.ID == id {
			tm.tasks = append(tm.tasks[:i], tm.tasks[i+1:]...)
			return
		}
	}
}

// ListTasks 列出所有任务
func (tm *TaskManager) ListTasks() {
	for _, task := range tm.tasks {
		status := "未完成"
		if task.Completed {
			status = "已完成"
		}
		fmt.Printf("任务ID: %d, 名称: %s, 状态: %s, 创建时间: %s\n", task.ID, task.Name, status, task.CreatedAt.Format(time.RFC1123))
	}
}

func main() {
	taskManager := &TaskManager{}

	taskManager.AddTask("学习Go语言")
	taskManager.AddTask("完成作业")
	taskManager.AddTask("锻炼身体")

	fmt.Println("所有任务:")
	taskManager.ListTasks()

	taskManager.CompleteTask(1)

	fmt.Println("\n标记任务ID为1的任务为完成后的所有任务:")
	taskManager.ListTasks()

	taskManager.DeleteTask(2)

	fmt.Println("\n删除任务ID为2的任务后的所有任务:")
	taskManager.ListTasks()
}
