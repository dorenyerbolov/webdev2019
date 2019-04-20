import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { ITaskList, ITask } from '../shared/models/models';

@Component({
  selector: 'app-parent',
  templateUrl: './parent.component.html',
  styleUrls: ['./parent.component.css']
})
export class ParentComponent implements OnInit {

  public output = '';
  public stringArray: string[] = [];

  public taskLists: ITaskList[] = [];
  public tasks: ITask[] = [];
  public curTaskList = '';
  public loading = false;

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then( res => {
      this.taskLists = res;
      this.loading = true;
    }); 
  }

  getTasks(taskList: ITaskList) {
    this.provider.getTasks(taskList).then( res => {
      this.curTaskList = taskList.name;
      this.tasks = res;
    })
  }

}
