import { Component } from '@angular/core';
import {MatIconModule} from '@angular/material/icon';
import {MatMenuModule} from '@angular/material/menu';
import {MatButtonModule} from '@angular/material/button';
import {MatDividerModule} from '@angular/material/divider';
import {MatToolbarModule} from '@angular/material/toolbar';
import { RouterModule } from '@angular/router';



@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    MatButtonModule,
    MatMenuModule,
    MatIconModule,
    MatDividerModule,
    MatToolbarModule,
    RouterModule
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
})
export class HomeComponent {

  protected readonly appHeader = 'Family Server UI';
  protected readonly eventTrackerMenuLabel = 'Event Tracker';
  protected readonly financeMenuLabel = 'Finance';
  protected readonly homePageContent = `
    Welcome to family server UI.
    <br>Select the menu for appropriate actions.
    <br>For any queries/questions please contact server admins.
  `;

}
