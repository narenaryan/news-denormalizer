--
-- Name: publisher; Type: TABLE; Schema: usa; Owner: root
--

CREATE TABLE usa.publisher (
    name character varying NOT NULL
);


ALTER TABLE usa.publisher OWNER TO root;

--
-- Name: publisher publisher_pkey; Type: CONSTRAINT; Schema: usa; Owner: root
--

ALTER TABLE ONLY usa.publisher
    ADD CONSTRAINT publisher_pkey PRIMARY KEY (name);