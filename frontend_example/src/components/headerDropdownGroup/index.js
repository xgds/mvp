import React from "react";
import HeaderDropdown from "../headerDropdown";
import "./style.css";

class HeaderDropdownGroup extends React.Component {
    render() {
        return (
            <span className="header-dropdown-group">
                <HeaderDropdown />
                <HeaderDropdown />
                <HeaderDropdown />
            </span>
        );
    }
}

export default HeaderDropdownGroup;