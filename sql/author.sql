--
-- Name: author; Type: TABLE; Schema: usa; Owner: root
--

CREATE TABLE usa.author (
    name character varying NOT NULL
);


ALTER TABLE usa.author OWNER TO root;

--
-- Name: author author_pkey; Type: CONSTRAINT; Schema: usa; Owner: root
--

ALTER TABLE ONLY usa.author
    ADD CONSTRAINT author_pkey PRIMARY KEY (name);

