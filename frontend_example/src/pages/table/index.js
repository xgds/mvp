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

import CardTabularContent from "../../components/cardTabularContent";
import CardContent from "../../components/cardContent";

// redux storage
import { createStore } from 'redux';

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
        this.flightsStore = createStore(this.storage);
    }

    render() {
        return (
            <div className="dashboard">
                <Navigation />
                <Sidebar
                    className="left"
                    content="flights"
                    store={this.flightsStore}
                />
                <Content
                    className="middle"
                    content={
                        <CardTabularContent
                            footer={this.props.footer}
                            store={this.store}
                        />
                    }
                    store={this.store}
                    footer={false}
                />
                <Content
                    className="right"
                    content={
                        <CardContent
                            footer={this.props.footer}
                            store={this.store}
                        />
                    }
                    store={this.store}
                    footer={true}
                />
            </div>
        );
    }

    componentDidMount() {
        // pass
    }
}

ReactDOM.render(<Dashboard />, document.getElementById("index"));