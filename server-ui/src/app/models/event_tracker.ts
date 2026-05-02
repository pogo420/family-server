
/**
 * Event interface defines the structure of an event object. 
 * It includes the event ID, name, date(0-31), and month(0-12).
 */
export interface Event {
  event_id: string;
  event_name: string;
  event_date: string;
  event_month: string;
}

/**
 * EventPayload interface defines the structure of the payload required to add a new event. 
 * It includes the event name, date(0-31), and month(0-12). 
 */
export interface EventPayload {
  event_name: string;
  event_date: string;
  event_month: string;
}
