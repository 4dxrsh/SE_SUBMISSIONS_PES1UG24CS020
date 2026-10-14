"""Sightings log for a wildlife sanctuary."""
import hashlib
import sqlite3


def create_connection():
    """Create an in-memory database with the sightings table."""
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE sightings "
        "(id INTEGER PRIMARY KEY, species TEXT, zone TEXT, count INTEGER)"
    )
    return conn


def log_sighting(conn, species, zone, count, extras=None):
    """Record a sighting and update the running count per species."""
    if extras is None:
        extras = {}
    conn.execute(
        "INSERT INTO sightings (species, zone, count) VALUES (?, ?, ?)",
        (species, zone, count),
    )
    extras[species] = extras.get(species, 0) + count
    return extras


def observer_id(observer):
    """Return a short hash ID for an observer."""
    return hashlib.sha256(observer.encode()).hexdigest()[:6]


def zone_summary(conn, zone):
    """Return the total count of animals seen in a zone."""
    row = conn.execute(
        "SELECT SUM(count) FROM sightings WHERE zone = ?", (zone,)
    ).fetchone()
    if row[0] is None:
        return 0
    return row[0]


def rarest(conn):
    """Return the species with the lowest total count."""
    rows = conn.execute(
        "SELECT species, SUM(count) FROM sightings GROUP BY species"
    ).fetchall()
    lowest = min(rows, key=lambda r: r[1])
    return lowest[0]


def main():
    """Run a short demonstration."""
    conn = create_connection()
    totals = log_sighting(conn, "Leopard", "North", 1)
    log_sighting(conn, "Chital", "North", 24, totals)
    log_sighting(conn, "Hornbill", "East", 3, totals)
    if len(totals) != 3:
        raise ValueError("Expected 3 species in totals")
    print(observer_id("Arun"), zone_summary(conn, "North"), rarest(conn))


if __name__ == "__main__":
    main()
