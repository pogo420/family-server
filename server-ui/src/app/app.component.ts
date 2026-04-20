import { Component } from '@angular/core';

import { RouterOutlet } from '@angular/router';
import { NavBarComponent } from './components/nav-bar/nav-bar.component';
import { EntryCommentComponent } from './components/entry-comment/entry-comment.component';

@Component({
    selector: 'app-root',
    imports: [
    RouterOutlet,
    NavBarComponent,
    EntryCommentComponent
],
    templateUrl: './app.component.html',
    styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'server-ui';
}
