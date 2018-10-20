import "./style.css";
import React from "react";

// sidebar list component
import SidebarList from "../sidebarList";

class Sidebar extends React.Component {
    constructor(props) {
        super(props);
        this.content = props.content;
    }

    render() {
        return (
            <div className="sidebar">
                <div>
                    <h5>Flights</h5>
                    <SidebarList
                        flightStore={this.props.flightStore}
                        content={this.content}
                    />
                </div>
            </div>
        );
    }
}

export default Sidebar;
