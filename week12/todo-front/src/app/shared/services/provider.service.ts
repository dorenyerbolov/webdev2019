import {
  Injectable,
  EventEmitter
} from "@angular/core";
import {
  HttpClient
} from "@angular/common/http";
import {
  MainService
} from "./main.service";
import {
  ITaskList,
  ITask
} from "../models/models";

@Injectable({
  providedIn: "root"
})
export class ProviderService extends MainService {
  public sendMessage = new EventEmitter<string>();

  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<ITaskList[]> {
    return this.get("http://127.0.0.1:8000/task_lists/", {});
  }

  getTasks(taskList: ITaskList): Promise<ITask[]> {
    return this.get(
      `http://127.0.0.1:8000/task_lists/${taskList.id}/tasks/`, {}
    );
  }

  updateTaskList(taskList: ITaskList): Promise<ITaskList> {
    return this.put(`http://127.0.0.1:8000/task_lists/${taskList.id}/`, {
      name: taskList.name
    });
  }

  deleteTaskList(taskList: ITaskList): Promise<ITaskList> {
    return this.delete(`http://127.0.0.1:8000/task_lists/${taskList.id}/`, {});
  }

  createTaskList(taskName: any): Promise<ITaskList> {
    return this.post('http://127.0.0.1:8000/task_lists/', {
      name: taskName
    });
  }
}