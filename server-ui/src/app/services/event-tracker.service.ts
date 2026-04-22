import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { map, Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { EVENT_ALL, EVENT_TRACKER } from '../constants/event_tracker';
import { Event, EventPayload } from '../models/event_tracker';

@Injectable({
  providedIn: 'root',
})
export class EventTrackerService {

  constructor(private http: HttpClient) {}

  /**
   * Service logic to show all events
   * This method sends a GET request to the server to retrieve all events and maps the response to an array of Event objects.
   * @returns An Observable of an array of Event objects
   */
  showAllEvents(): Observable<Event[]> {
    // Implement logic to show all events
    return this.http.get<Event[]>(environment.restBaseUrl + EVENT_ALL).pipe(
      map((response: any) => {
        // Assuming the response is an array of events
        return response.map((event: any) => ({
          event_id: event.event_id,
          event_name: event.event_name,
          event_date: event.day,
          event_month: event.month,
        }));
      })
    );
  }

  /**
   * Service logic to delete an event by its ID
   * This method constructs the necessary parameters and sends a DELETE request to the server to remove the specified event.
   * @param eventId The ID of the event to delete
   * @returns An Observable of the HTTP response from the server
   */
  deleteEvent(eventId: string): Observable<Object> {
    const params = new HttpParams()
      .set('event_id', eventId)
    return this.http.delete(environment.restBaseUrl + EVENT_TRACKER, {
      params
    });
  }

  /** Service logic to add event
   * @param event - The event payload containing event_name, event_date, and event_month
   * @returns An Observable of the HTTP response from the server
   * This method constructs the event payload and sends a POST request to the server to add a new event.
   */
  addEvent(event: EventPayload): Observable<Object> {
    const event_payload = {
      event_name: event.event_name,
      day: event.event_date,
      month: event.event_month
    }
    return this.http.post(environment.restBaseUrl + EVENT_TRACKER, event_payload);
  }
  
}
