// react + react dom
import React from "react";
import ReactDOM from "react-dom";

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

// redux storage
import { createStore } from 'redux';
import OpenLayersMap from "../../components/openLayersMap";

// dashboard react component
class Dashboard extends React.Component {
    storage(state = undefined, action) {
        if (state === undefined)
        {
            // this is the default state of the dashboard
            state = {};
        }
        switch(action.type) {
            case 'change-selection':
                return action.action;
            default:
                break;
        }
        return state;
    }

    constructor(props) {
        super(props);
        this.store = createStore(this.storage);
    }

    render() {
        return (
            <div className="dashboard">
                <Navigation />
                <Sidebar
                    className="left"
                    content="flights"
                    store={this.store}
                />
                <Content
                    className="middle"
                    content={                
                        <OpenLayersMap 
                            store={this.store}
                        />
                    }
                    store={this.store}
                    footer={true}
                    header={false}
                />
                <Content
                    className="right"
                    content={
                        <CardContentTable
                            store={this.store}
                        />
                    }
                    store={this.store}
                    footer={true}
                    header={true}
                />
            </div>
        );
    }
}

ReactDOM.render(<Dashboard />, document.getElementById("index"));