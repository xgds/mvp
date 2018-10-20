// react + react dom
import React from "react";
import ReactDOM from "react-dom";
import { Button } from 'reactstrap';
// jquery
import $ from "jquery";

// css
import "../../css/dashboard.css";
import 'bootstrap/dist/css/bootstrap.min.css';

// react classes inside 'components' folder
import Navigation from "../../components/navigation";
import Sidebar from "../../components/sidebar";
import Content from "../../components/content";
import CardContentTable from "../../components/cardContentTable";
import MapPopover from "../../components/mapPopover";

// redux storage
import { createStore } from 'redux';
import OpenLayersMap from "../../components/openLayersMap";

// dashboard react component
class Dashboard extends React.Component {
    flightStorage(state = undefined, action) {
        if (state === undefined)
        {
            // this is the default state of the dashboard
            state = {enabledFlights: [], allFlights: []};
        }
        switch(action.type) {
            case 'add-flights':
                return {
                    allFlights: action.flights,
                    enabledFlights: [], // might change later
                };
            case 'enable-flight':
                return {
                    allFlights: state.allFlights,
                    enabledFlights: [action.flight].concat(state.enabledFlights),
                };
            case 'disable-flight':
                return {
                    allFlights: state.allFlights,
                    enabledFlights: state.enabledFlights.filter(x => x != action.flight),
                };
            default:
                break;
        }
        return state;
    }

    objectStorage(state = undefined, action) {
        if (state === undefined)
        {
            // this is the default state of the dashboard
            state = {
                objects: [],
                filteredObjects: [],
            };
        }
        switch(action.type) {
            case 'add-objects':
                return {
                    objects: action.objects.concat(state.objects),
                    filteredObjects: state.filteredObjects,
                };
            case 'filter-objects':
                return {
                    objects: state.objects,
                    filteredObjects: action.filteredObjects,
                }
            default:
                break;
        }
        return state;
    }

    popoverStorage(state = undefined, action) {
        if (state === undefined)
        {
            // this is the default state of the dashboard
            state = {
                text: "Loading...",
            };
        }
        switch(action.type) {
            case 'change-text':
                return {
                    text: action.text,
                };
            default:
                break;
        }
        return state;
    }

    constructor(props) {
        super(props);

        // flights and objects stores
        this.flightStore = createStore(this.flightStorage);
        this.objectStore = createStore(this.objectStorage);

        // map popover store
        this.popoverStore = createStore(this.popoverStorage);

        // when: a change is made to the enabled flights
        // then: correct the filtered objects array accordingly
        this.flightStore.subscribe(function () {
            let enabledFlights = this.flightStore.getState().enabledFlights;
            let allObjects = this.objectStore.getState().objects;
            let filteredObjects = allObjects.filter(x => enabledFlights.includes(x.flight.$oid));
            this.objectStore.dispatch({
                type: 'filter-objects',
                filteredObjects: filteredObjects,
            });
        }.bind(this));
    }

    componentDidMount() {
        // fetch all flights
        $.getJSON("http://localhost:5000/flight", function(data) {
            this.flightStore.dispatch({
                type: "add-flights",
                flights: data,
            });
        }.bind(this));

        // fetch all objects
        $.getJSON("http://localhost:5000/object", function (data) {
            this.objectStore.dispatch({
                type: 'add-objects',
                objects: data,
            });
        }.bind(this));
    }

    render() {
        return (
            <div className="dashboard">  
                <Navigation />
                <Sidebar
                    className="left"
                    content="flights"
                    flightStore={this.flightStore}
                />
                <Content
                    className="middle"
                    content={
                        <CardContentTable
                            numberOfRows={18}
                            objectStore={this.objectStore}
                        />
                    }
                    footer={false}
                    header={true}
                />
                <Content
                    className="right"
                    content={                
                        <OpenLayersMap 
                            objectStore={this.objectStore}
                            popoverStore={this.popoverStore}
                        />
                    }
                    footer={true}
                    header={false}
                />
                <MapPopover
                    popoverStore={this.popoverStore}
                />
            </div>
        );
    }
}

ReactDOM.render(<Dashboard />, document.getElementById("index"));