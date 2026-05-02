import { Component, ChangeDetectorRef, ChangeDetectionStrategy } from '@angular/core';
import { EventTrackerService } from '../../services/event-tracker.service';
import { Event } from '../../models/event_tracker';
import {MatIconModule} from '@angular/material/icon';
import {MatTableModule} from '@angular/material/table';
import {MatButtonModule} from '@angular/material/button';
import { MatDialog } from '@angular/material/dialog';
import { AddEventComponent } from './add-event/add-event.component';



@Component({
  selector: 'app-event-tracker',
  imports: [MatIconModule, MatTableModule, MatButtonModule],
  templateUrl: './event-tracker.component.html',
  styleUrl: './event-tracker.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class EventTrackerComponent {

  constructor(private eventService: EventTrackerService, private cd: ChangeDetectorRef, private dialog: MatDialog) { }

  protected displayedColumns: string[] = [
    'event_date', 'event_name', 'delete'
  ];
  protected events: Event[] = [];

  protected eventTableHeader: string = 'Events';
  protected dateColumnHeader: string = 'Date';
  protected nameColumnHeader: string = 'Event Name';
  

  ngOnInit() {
    this.fetchEventData();
  }

  protected deleteEvent(event_id: string) {
    console.log('delete event with id:', event_id);
    this.deleteEventData(event_id);
  }


  private fetchEventData(): void {
    this.eventService.showAllEvents().subscribe(
      {
        next: (data) => {
          console.log('fetched event data:', data);
          this.events = data;
          this.cd.markForCheck();
        },
        error: (err) => console.error(err),
        complete: () => console.log('fetched event data successfully')
      }
    );
  }

  private deleteEventData(eventId: string): void{
    this.eventService.deleteEvent(eventId).subscribe(
      {
        next: (response) => {
          console.log('deleted:', eventId);
          this.fetchEventData();
        },
        error: (err) => console.error(err)
      }
    )
  }

  // Method to open the add event dialog
  protected addUserDialog() {
    console.log('add user dialog');
      const dialogRef = this.dialog.open(AddEventComponent, {
    width: '400px'
  });

  dialogRef.afterClosed().subscribe(result => {
    if (result) {
      console.log('User data:', result);
      // call API or update list here
      this.eventService.addEvent(result).subscribe(
        {
          next: (response) => {
            console.log('added event:', response);
            this.fetchEventData();
          },
          error: (err) => console.error(err)
        }
      );
    }
  });
  }


}
