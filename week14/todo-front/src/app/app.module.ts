import { BrowserModule } from '@angular/platform-browser';
import { NgModule, ClassProvider } from '@angular/core';

import { AppComponent } from './app.component';
import { AuthInterceptor } from './interceptors/AuthInterceptor';
import { ParentComponent } from './components/parent/parent.component';  
import { ProviderService} from './services/provider.service'
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule } from '@angular/forms'

@NgModule({
  declarations: [
    AppComponent,
    ParentComponent,
  ],
  imports: [
    FormsModule,
    BrowserModule,
    HttpClientModule
  ], 
  providers: [ProviderService,
  <ClassProvider> {
    provide: HTTP_INTERCEPTORS,
    useClass: AuthInterceptor,
    multi: true
  }],
  bootstrap: [AppComponent]
})
export class AppModule { }
