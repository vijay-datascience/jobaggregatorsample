{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "import psycopg2\n",
    "\n",
    "def create_tables():\n",
    "#\"\"\" create tables in the PostgreSQL database\"\"\"\n",
    "    command = (\n",
    "        \"\"\"\n",
    "        CREATE TABLE jobads (\n",
    "            jobid SERIAL PRIMARY KEY,\n",
    "            URL VARCHAR(255) NOT NULL,\n",
    "            Title VARCHAR(255),\n",
    "            Company VARCHAR(100),\n",
    "            Exp VARCHAR(10),\n",
    "            Location VARCHAR(200),\n",
    "            Rating VARCHAR(4)\n",
    "        )\n",
    "        \"\"\")\n",
    "    conn = None\n",
    "    try:\n",
    "        # connect to the PostgreSQL server\n",
    "        conn = psycopg2.connect(\"host=localhost dbname=postgres user=postgres password=<password>\")\n",
    "        cur = conn.cursor()\n",
    "        # create table one by one\n",
    "        cur.execute(command)\n",
    "        # close communication with the PostgreSQL database server\n",
    "        cur.close()\n",
    "        # commit the changes\n",
    "        conn.commit()\n",
    "    except (Exception, psycopg2.DatabaseError) as error:\n",
    "        print(error)\n",
    "    finally:\n",
    "        if conn is not None:\n",
    "            conn.close()\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    create_tables()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
