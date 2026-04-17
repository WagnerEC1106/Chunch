// admin_captian_shared.js

export function formatCountLabel(count) {
    return count === 1 ? "1 volunteer" : `${count} volunteers`;
}

export function getVolunteerDisplayName(volunteer) {
    if (typeof volunteer === "string") return volunteer;
    return volunteer.name || `${volunteer.firstName || ""} ${volunteer.lastName || ""}`.trim();
}

export function isCaptain(volunteer) {
    if (!volunteer || typeof volunteer === "string") return false;

    const captainStatus = (volunteer.captain_status || volunteer.captainStatus || "").toString().toLowerCase();
    const role = (volunteer.role || "").toString().toLowerCase();

    return captainStatus === "captain" || role === "captain";
}

export function isAdmin(volunteer) {
    if (!volunteer || typeof volunteer === "string") return false;
    return (volunteer.role || "").toString().toLowerCase() === "admin";
}