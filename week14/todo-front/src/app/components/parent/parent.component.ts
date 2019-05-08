import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import { ProviderService } from '../../services/provider.service';
import { ITaskList, ITask } from '../../models/models';

@Component({
  selector: 'app-parent',
  templateUrl: './parent.component.html',
  styleUrls: ['./parent.component.css']
})
export class ParentComponent implements OnInit {

  public output = '';
  public taskName = '';
  public stringArray: string[] = [];

  public taskLists: ITaskList[] = [];
  public tasks: ITask[] = [];
  public curTaskList = '';
  public loading = false;
  public loggedIn = false;

  public username: any = '';
  public password: any = '';

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    let token = localStorage.getItem('token')
    if (token) {
      this.loggedIn = true;
    }

    if (this.loggedIn) {
      this.provider.getTaskLists().then( res => {
        this.taskLists = res;
        this.loading = true;
      }); 
    }
  }

  getTasks(taskList: ITaskList) {
    this.provider.getTasks(taskList).then( res => {
      this.curTaskList = taskList.name;
      this.tasks = res;
    })
  }

  updateTaskList(taskList: ITaskList) {
    this.provider.updateTaskList(taskList).then( res => {
      console.log(`${taskList.name} updated`);
    })
  }

  deleteTaskList(taskList: ITaskList) {
    this.provider.deleteTaskList(taskList).then( res => {
      console.log(`${taskList.name} deleted`);
      this.provider.getTaskLists().then( res => {
        this.taskLists = res;
      })
    })
  }

  createTaskList() {
    if (this.taskName != '') {
      this.provider.createTaskList(this.taskName).then( res => {
        this.taskName = '';
        this.taskLists.push(res);
      })
    }
  }

  auth() {
    if (this.username !== '' && this.password !== ''){
      this.provider.auth(this.username, this.password).then( res => {
        localStorage.setItem('token', res.token);

        this.loggedIn = true;

        this.provider.getTaskLists().then( res => {
          this.taskLists = res;
          this.loading = true;
        }); 
      })
    }
  }

  logout() {
    this.provider.logout().then( res => {
      localStorage.removeItem('token');
      this.loggedIn = false;
    })
  }

}
